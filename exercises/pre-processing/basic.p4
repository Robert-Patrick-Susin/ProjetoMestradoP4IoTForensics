/* -*- P4_16 -*- */
#include <core.p4>
#include <v1model.p4>

const bit<16> TYPE_IPV4 = 0x800;
const bit<8> RECIRC_FL_1 = 3;
const bit<16> TYPE_AGG = 0x1212;

#define PKT_INSTANCE_TYPE_INGRESS_RECIRC 4
#define PKT_INSTANCE_TYPE_NORMAL 0
#define MAX_IOT_AGG 8

/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/

typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;

register<bit<32>>(1) pontador;
register<bit<32>>(8) banco;

header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16>   etherType;
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
    @field_list(RECIRC_FL_1)
    bit<8>    m_pproc_01;
    @field_list(RECIRC_FL_1)
    bit<8>    m_pproc_02; 
    @field_list(RECIRC_FL_1)
    bit<32>   total_rodadas;
    @field_list(RECIRC_FL_1)
    bit<8>    proximo_pproc;
    @field_list(RECIRC_FL_1)
    bit<32>   rodadas;
    @field_list(RECIRC_FL_1)
    bit<8>    pkt_agg;
    @field_list(RECIRC_FL_1)
    bit<8>    pkt_agregador;
    @field_list(RECIRC_FL_1)
    bit<8>    pkt_filtrado; 
    @field_list(RECIRC_FL_1)
    bit<8>    banco_cheio;
    @field_list(RECIRC_FL_1)
    bit<32>   pointer;
    @field_list(RECIRC_FL_1)
    bit<32>   iterador;
    @field_list(RECIRC_FL_1)
    bit<8>    passou_rodada_0;
    @field_list(RECIRC_FL_1)
    bit<8>    pkt_agregado;
}

struct headers {
    ethernet_t                      ethernet;
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
            TYPE_AGG: parse_iot_agregacao;
            default: parse_ipv4;
        }
    }

    state parse_iot_agregacao {
        packet.extract(hdr.iot_agregacao.next);
        transition select(hdr.iot_agregacao.last.next_hdr) {
			0: parse_ipv4;
            1: parse_iot_agregacao;
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
    }

    /*Escreve payload iot_leituras dentro da posiçao pointer no registrador banco*/
    action escreve_banco() {
        banco.write(meta.pointer, (bit<32>)hdr.ipv4.dstAddr);
    }

    /*
    Isso ocorre pela funçao push_front que empurra todas posiçoes 1 casa a direita do vetor iot_agregacao{2}, e a nova posiçao apontada agora e 0, 
    a ultima ficara na 1, assim populando as posiçoes consecutivas do "mesmo" cabeçalho composto
    Essa nova posiçao e invalida, por isso e necessario setValid para seta-la como valida e sendo por hr undefined
    Usado meta.iterador para recebimento pelo novo cabeçalho iot_agregacao na posicao reposicionada sendo 0, no vlr iot_leituras para o iot_agg.
    */
    action escreve_banco_em_iot_agg() {
        hdr.iot_agregacao.push_front(1);
        hdr.iot_agregacao[0].setValid();
        /*Declara variavel local para armazenar o payload*/
        bit<32> armazena_payload = 0;
        /*Armazena na variavel armazena_payload o vlr do registrador Banco na posicao meta.iterador*/
        banco.read(armazena_payload, meta.iterador);
        /*Armazena na variavel iot_agg o vlr do payload em armazena_payload*/
        hdr.iot_agregacao[0].iot_agg = (bit<16>)armazena_payload;
        /*Soma 1 no iterador para pegar a proxima posicao na proxima iteraçao*/
        meta.iterador = meta.iterador + 1;
    }

    /*Biblioteca + Tabela de módulos*/
    action biblioteca(bit<8> m_pproc_01, bit<8> m_pproc_02, bit<32> ttl_rodadas) {
        clone(CloneType.I2E, (bit<32>)1);
        meta.m_pproc_01  =  m_pproc_01;
        meta.m_pproc_02  =  m_pproc_02;
        meta.total_rodadas = ttl_rodadas;
    }

    table mapeamento{
        key = {
            hdr.ipv4.srcAddr: lpm;
        }
        actions = {
            biblioteca;
        }
           size = 1024;
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
        /*Verifica se a rodada é a primeira, se for realiza match+action IPV4 & Mapeamento. Também verifica se o pacote já passou por aqui,
        caso for recirculado ele dará false nessa verificação de metadado qual é preenchido no final dessse If*/
        if (meta.rodadas == 0 && meta.passou_rodada_0 == 0){
            if (hdr.ipv4.isValid()) {
                ipv4_lpm.apply();
            }

            /*Executa tabela de mapeamento e biblioteca para mapear a ordem de pré-processamento que o usuário inseriu*/ 
            mapeamento.apply();

            /*Metadado de próximo módulo de pré-processamento recebe a primeira função ser executada*/
            meta.proximo_pproc = meta.m_pproc_01;

            /*Metadado para marcar que a rodada 0 já foi executada e assim em recirculações ela dará false para rodada 0*/
            meta.passou_rodada_0 = 1;
        }

        /*Senão se a rodada é a segunda, ajeita segunda função a ser executada*/
        else if (meta.rodadas == 1){
            
            /*Metadado de próximo módulo de pré-processamento recebe a segunda função ser executada*/
            meta.proximo_pproc = meta.m_pproc_02;
            /*Forçar porta de saída para host 42 (Plano de Controle / Blockchain) como medida de contingências para caso houver somente filtragem*/
            standard_metadata.egress_spec = 42;
        }

        /*Se a rodada atingiu o total, adiciona metadado de próximo pproc como 0 para passar reto pelos pré-processamentos*/
        else if (meta.rodadas == meta.total_rodadas){
            meta.proximo_pproc = 0;
            /*Forçar porta de saída para host 42 (Plano de Controle / Blockchain)*/
            standard_metadata.egress_spec = 42;
        }            

        /*Código da Agregação*/
        /*Primeira verificação com comparação ao identificador de Agregação com a próxima função a ser executada (Agregação = 1), se for inicia módulo Agregação*/
        if (meta.proximo_pproc == 1) {

            /*Pacote chega, é um pacote agregador? Ou seja, já foi anteriormente recirculado, e logo, o Banco está Cheio? Se sim escreve banco*/
            if (meta.pkt_agregador == 1) {
            escreve_banco_em_iot_agg();

            /*Esse pacote marcará o metadado Banco cheio como vazio, pois é importante que enquanto ele for recirculado ele próprio não entre no último decisor e crie loop*/
            meta.banco_cheio = 0;

                /*Decisor para ordenar cabeçalhos*/
                if (meta.iterador == 1) {
                    /*Cabeçalho sinaliza que é um pacote agregado para ser parseado nas suas próximas recirculações e iterações*/
                    hdr.ethernet.etherType = TYPE_AGG;
                    /*Sinalizamos que nessa primeira iteração como o cabeçalho é [0], o próx hdr é IPv4*/
                    hdr.iot_agregacao[0].next_hdr = 0;
                }
                else {
                    /*Demais iterações [1]...[n] o próx hdr é agregação*/
                    hdr.iot_agregacao[0].next_hdr = 1;
                }
            }

            /*Senão for um pacote agregador, ou seja, marcado e recirculado, o banco não está cheio ainda, continua copiando*/
            else {

                /*Le pontador e incrementa*/
                pontador.read(meta.pointer, 0);
                if (meta.pointer < 7){
                        meta.pointer = meta.pointer + 1;
                }

                /*Se ele estiver cheio zera para recomeçar*/
                else {
                    meta.pointer = 0;
                }

                /*Sempre escreve no registrador pontador na posiçao 0 vlr meta.pointer*/
                pontador.write(0, meta.pointer);

                /*Sempre chama funçao de escrever payload no banco*/
                escreve_banco();

                /*Se o banco estiver cheio, realizamos as marcações pkt de agregação e banco cheio*/
                if (meta.pointer == 0){
                    meta.pkt_agg = 1;
                    meta.banco_cheio = 1;
                }

                /*Senão será descartado, pois já cumpriu seu dever de ser escrito no registrador banco*/
                else {
                    drop();
                }
            }
        }
        /*Código de Filtragem*/
        /*Segunda verificação com comparação ao identificador de Filtragem com a próxima função a ser executada (Filtragem = 2)*/
        if (meta.proximo_pproc == 2) {
            /*Coloca metadado que marca filtragem para dar sequência em sua lógica*/
            // meta.pkt_filtrado = 1;
            /* Por hora filtragem só dropa pacote */
            drop();
        }
    }
}

/*************************************************************************
****************  E G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyEgress(inout headers hdr,
                 inout metadata meta,
                 inout standard_metadata_t standard_metadata) {                   
    apply {
        /*O pacote que chega pertence ao módulo 1 Agregação? Se sim executa lógica Agg*/
        if (meta.pkt_agg == 1){

            /*Se contador responsavel por dizer se pacote agregado esta cheio ainda nao for X, ou seja, n estiver cheio e tambem e maior que 0, ou seja,
            ja foi recirculado ao menos 1 vez, entao recircula novamente ate encher*/
            if (meta.iterador < 8 && meta.iterador > 0) {
                recirculate_preserving_field_list(RECIRC_FL_1);
            }

            /*Agora uma vez que esse contador é igual a X, ou seja, cabeçalhos de agregaçao cheios, removo metadado que marca como pré-processado por 1 (Agregação)
             & Soma +1 no Round, e recircula para executar próximo pré-processamento*/
            else {
                if (meta.iterador == 8) {   
                    meta.pkt_agg = 0;
                    meta.rodadas = meta.rodadas + 1;
                    recirculate_preserving_field_list(RECIRC_FL_1);
                }
            }

            /*Se houver metadado de banco cheio, o contador que diz se o pacote agregado esta cheio sera zerado. O pacote
            será marcado como agregador para iniciar lógica agregação em vetores no Ingress e o pacote será recirculado pela primeira vez dentro da lógica de Agregação*/
            if (meta.banco_cheio == 1) {
                meta.iterador = 0;
                meta.pkt_agregador = 1;
                recirculate_preserving_field_list(RECIRC_FL_1);
            }
        }

        /*O pacote que chega pertence ao módulo 2 Filtragem? Se sim executa lógica Filt*/
        if (meta.pkt_filtrado == 1){
            
            /*Lógica que aplica filtragem, por hora ela somente descarta no Ingress, mas lá e aqui poderia realizar outras coisas*/

            /*Remove Metadado que marca como pré-processado por 2 (Filtragem) & Soma +1 no Round*/
            meta.pkt_filtrado = 0;
            meta.rodadas = meta.rodadas + 1;

            /*Lógica PRIME, recircula quando terminar para próximo programa, mas a filtragem é sempre o último programa independente da ordem*/
            recirculate_preserving_field_list(RECIRC_FL_1);
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
