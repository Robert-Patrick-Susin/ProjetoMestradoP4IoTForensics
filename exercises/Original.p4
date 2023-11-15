Original
/* -*- P4_16 -*- */
#include <core.p4>
#include <v1model.p4>

const bit<16> TYPE_IOTPROTOCOL = 0x1212;
const bit<16> TYPE_IPV4 = 0x800;

#define PKT_INSTANCE_TYPE_INGRESS_RECIRC 4
#define MAX_IOT_AGG 3

/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/

typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;

register<bit<32>>(1) pontador;
register<bit<32>>(3) banco;
register<bit<32>>(1) iterador;

header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16>   etherType;
}

header iotprotocol_t {
    bit<16> iot_id;
    bit<16> iot_leituras;
    bit<16> next_hdr;
}

header iot_agregacao_t {
    bit<16> iot_agg;
    bit<16> next_hdr;
}

header ipv4_t {
    bit<4>    version;
    bit<4>    ihl;
    bit<8>    diffserv;
    bit<16>   totalLen;
    bit<16>   identification;
    bit<3>    flags;
    bit<13>   fragOffset;
    bit<8>    ttl;
    bit<8>    protocol;
    bit<16>   hdrChecksum;
    ip4Addr_t srcAddr;
    ip4Addr_t dstAddr;
}

struct metadata {
    bit<32> pointer;
    bit<32> iterador;
}

struct headers {
    ethernet_t                      ethernet;
    iotprotocol_t                   iotprotocol;
    ipv4_t                          ipv4;
    iot_agregacao_t[MAX_IOT_AGG]    iot_agregacao;
}

/*************************************************************************
*********************** P A R S E R  ***********************************
*************************************************************************/

parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {

    state start {
        transition parse_ethernet;
    }

    state parse_ethernet {
        packet.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            TYPE_IOTPROTOCOL: parse_iotprotocol;
            TYPE_IPV4: parse_ipv4;
            default: accept;
        }
    }

    state parse_iotprotocol {
        packet.extract(hdr.iotprotocol);
        transition select (standard_metadata.instance_type) {
            PKT_INSTANCE_TYPE_INGRESS_RECIRC: parse_iot_agregacao;
            default: parse_ipv4;
        }
    }

    state parse_iot_agregacao {
        packet.extract(hdr.iot_agregacao.next);
        transition select(hdr.iot_agregacao.last.next_hdr) {
			0: parse_ipv4;
            1: parse_iot_agregacao;
			default: accept;
		}
    }

    state parse_ipv4 {
        packet.extract(hdr.ipv4);
        transition accept;
    }

}

/*************************************************************************
************   C H E C K S U M    V E R I F I C A T I O N   *************
*************************************************************************/

control MyVerifyChecksum(inout headers hdr, inout metadata meta) {
    apply {  }
}


/*************************************************************************
**************  I N G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyIngress(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {
    action drop() {
        mark_to_drop(standard_metadata);
    }

    action ipv4_forward(macAddr_t dstAddr, egressSpec_t port) {
        standard_metadata.egress_spec = port;
        hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
        hdr.ethernet.dstAddr = dstAddr;
        hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
        hdr.iotprotocol.next_hdr = 0;
    }

    /*Escreve payload iot_leituras dentro da posiçao pointer no registrador banco*/
    action escreve_banco() {
        banco.write(meta.pointer, (bit<32>)hdr.iotprotocol.iot_leituras);
    }

    /*
    Isso ocorre pela funçao push_front que empurra todas posiçoes 1 casa a direita do vetor iot_agregacao{2}, e a nova posiçao apontada agora e 0, 
    a ultima ficara na 1, assim populando as posiçoes consecutivas do "mesmo" cabeçalho composto
    Essa nova posiçao e invalida, por isso e necessario setValid para seta-la como valida e sendo por hr undefined
    Agora, e realizada leitura do payload iot_leituras armazenado no registrador banco na posicao meta.iterador para recebimento pelo
    novo cabeçalho iot_agregacao na posicao reposicionada sendo 0, no vlr iot_leituras para o iot_agg.
    */
    action escreve_banco_em_iot_agg() {
	 	iterador.read(meta.iterador, 0);
        hdr.iot_agregacao.push_front(1);
        hdr.iot_agregacao[0].setValid();
        /*Declara variavel local para armazenar o payload*/
        bit<32> armazena_payload = 0;
        /*Armazena na variavel aggregated_data o vlr da posicao meta.iterador*/
        banco.read(armazena_payload, meta.iterador);
        /*Armazena na variavel iot_agg o vlr do payload em armazena_payload*/
        hdr.iot_agregacao[0].iot_agg = (bit<16>)armazena_payload;
        /*Soma 1 no iterador para pegar a proxima posicao na proxima iteraçao*/
        meta.iterador = meta.iterador + 1;
        /*Armazena o novo vlr somado meta.iterador no registrador iterador na posiçao 0*/
        iterador.write(0, meta.iterador);
    }

    table ipv4_lpm {
        key = {
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            ipv4_forward;
            drop;
            NoAction;
        }
        size = 1024;
        default_action = drop();
    }
        
    apply {
        /*Pacote chega, é recirculado? Se sim escreve banco, se não continua*/
        if (standard_metadata.instance_type == PKT_INSTANCE_TYPE_INGRESS_RECIRC) {
            escreve_banco_em_iot_agg();
            /* Gambiarra para forçar porta de saída para host 42 (Plano de Controle) */
            standard_metadata.egress_spec = 42;
            /*Se meta.iterador == 'valor da primeira iteração' next_hdr = 0; Senão meta.iterador == 1*/
            if (meta.iterador == 1) {
                hdr.iot_agregacao[0].next_hdr = 0;
            }
            else {
                hdr.iot_agregacao[0].next_hdr = 1;
                hdr.iotprotocol.next_hdr = 1;
            }
        }
        else {
            if (hdr.ipv4.isValid()) {
                ipv4_lpm.apply();

                /*Somente Agregação*/
                /*Se for dispositivo IoT sensível realiza agregação*/
                //     /*Le pontador e incrementa*/
                //     pontador.read(meta.pointer, 0);
                //     if (meta.pointer < 3){
                //         meta.pointer = meta.pointer + 1;
                //     }
                //     /*Se ele estiver cheio, ou seja, = 3, zera para recomeçar*/
                //     else {
                //         meta.pointer = 0;
                //     }
                //     /*Sempre escreve no registrador pontador na posiçao 0 vlr meta.pointer */
                //     pontador.write(0, meta.pointer);
                //     /*Sempre chama funçao de escrever payload no banco*/
                //     escreve_banco();
                //     /*Se banco cheio clona de ingress para egress*/
                //     if (meta.pointer == 0){
                //         clone(CloneType.I2E, (bit<32>)1);
                //     }

                /*Somente Filtragem*/
                /*Se for dispositivo IoT sensível realize clone para posterior envio e gambiarra seta sua porta para host42 Blockchain*/
                // if (hdr.iotprotocol.iot_id == 1) {
                //     clone(CloneType.I2E, (bit<32>)1);
                // }

                /*Agregação + Filtragem*/
                /*Se for dispositivo IoT sensível realiza agregação*/
                if (hdr.iotprotocol.iot_id == 1) {
                    /*Le pontador e incrementa*/
                    pontador.read(meta.pointer, 0);
                    if (meta.pointer < 2){
                        meta.pointer = meta.pointer + 1;
                    }
                    /*Se ele estiver cheio, ou seja, = 3, zera para recomeçar*/
                    else {
                        meta.pointer = 0;
                    }
                    /*Sempre escreve no registrador pontador na posiçao 0 vlr meta.pointer */
                    pontador.write(0, meta.pointer);
                    /*Sempre chama funçao de escrever payload no banco*/
                    escreve_banco();
                    /*Se banco cheio clona de ingress para egress*/
                    if (meta.pointer == 0){
                        clone(CloneType.I2E, (bit<32>)1);
                    }
                }
            }
        }
    }
}

/*************************************************************************
****************  E G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyEgress(inout headers hdr,
                 inout metadata meta,
                 inout standard_metadata_t standard_metadata) {
                        
        action ipv4_forward(macAddr_t dstAddr, egressSpec_t port) {
            standard_metadata.egress_spec = port;
            hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
            hdr.ethernet.dstAddr = dstAddr;
            hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
        }

        table ipv4_lpm_gambia {
            key = {
                hdr.ipv4.dstAddr: lpm;
            }
            actions = {
                ipv4_forward;
            }
            size = 1024;
        }

    /*Apenas filtragem*/
    // apply {
    //     /*Se o pacote for clonado, significa que o dispositivo é sensível e envia para Blockchain*/
    //     if (standard_metadata.instance_type == 1) {
    //         ipv4_lpm_gambia.apply();
    //     }
    //   }

    // /*Somente Agregação*/
    // apply {
    //     /*Se contador responsavel por dizer se pacote agregado esta cheio ainda nao for 4, ou seja, n estiver cheio e tambem e maior que 0, ou seja,
    //     ja foi recirculado ao menos 1 vez, entao recircula novamente ate encher*/
    //     if (meta.iterador < 4 && meta.iterador > 0) {
    //         recirculate_preserving_field_list(0);
    //     }
    //     else {
    //         /*Agora uma vez que esse contador e igual a 4, ou seja, cabeçalhos de agregaçao cheios, envio para Blockchain*/
    //         if (meta.iterador == 4) {
    //             ipv4_lpm_gambia.apply();
    //         }
    //     }
    //     /*Se o pacote for clonado, significa que o banco esta cheio, logo, o contador que diz se o pacote agregado esta cheio sera zerado, e o pacote sera recirculado
    //     pela primeira vez*/
    //     if (standard_metadata.instance_type == 1) {
    //         meta.iterador = 0;
    //         iterador.write(0, 0);
    //         hdr.iot_agregacao[0].next_hdr = 0;
    //         recirculate_preserving_field_list(0);
    //     }
    //   }

    /*Agregação + Filtragem*/
    apply {
        /*Se contador responsavel por dizer se pacote agregado esta cheio ainda nao for 4, ou seja, n estiver cheio e tambem e maior que 0, ou seja,
        ja foi recirculado ao menos 1 vez, entao recircula novamente ate encher*/
        if (meta.iterador < 3 && meta.iterador > 0) {
            recirculate_preserving_field_list(0);
        }
        else {
            /*Agora uma vez que esse contador e igual a 4, ou seja, cabeçalhos de agregaçao cheios, envio para Blockchain*/
            if (meta.iterador == 3) {
                ipv4_lpm_gambia.apply();
            }
        }
        /*Se o pacote for clonado, significa que o banco esta cheio, logo, o contador que diz se o pacote agregado esta cheio sera zerado, e o pacote sera recirculado
        pela primeira vez*/
        if (standard_metadata.instance_type == 1) {
            meta.iterador = 0;
            iterador.write(0, 0);
            hdr.iot_agregacao[0].next_hdr = 0;
            recirculate_preserving_field_list(0);
        }
      }

}

/*************************************************************************
*************   C H E C K S U M    C O M P U T A T I O N   **************
*************************************************************************/

control MyComputeChecksum(inout headers  hdr, inout metadata meta) {
     apply {
        update_checksum(
        hdr.ipv4.isValid(),
            { hdr.ipv4.version,
              hdr.ipv4.ihl,
              hdr.ipv4.diffserv,
              hdr.ipv4.totalLen,
              hdr.ipv4.identification,
              hdr.ipv4.flags,
              hdr.ipv4.fragOffset,
              hdr.ipv4.ttl,
              hdr.ipv4.protocol,
              hdr.ipv4.srcAddr,
              hdr.ipv4.dstAddr },
            hdr.ipv4.hdrChecksum,
            HashAlgorithm.csum16);
    }
}

/*************************************************************************
***********************  D E P A R S E R  *******************************
*************************************************************************/

control MyDeparser(packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.iotprotocol);
        packet.emit(hdr.iot_agregacao);
        packet.emit(hdr.ipv4);
    }
}

/*************************************************************************
***********************  S W I T C H  *******************************
*************************************************************************/

V1Switch(
MyParser(),
MyVerifyChecksum(),
MyIngress(),
MyEgress(),
MyComputeChecksum(),
MyDeparser()
) main;
