#!/usr/bin/env python3
import os
import sys
import time
# import statistics

from myIoT_header import iotprotocol
from scapy.all import TCP, get_if_list, sniff

ultimo_tempo = time.time()

# Começo do experimento. Quando inicia o receptor
count = 0
tamanho_total = 0
# list_tempos = []


def get_if():
    ifs=get_if_list()
    iface=None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

# evento de recepção de pacote 
def handle_pkt(pkt):
    global count
    global tamanho_total
    # global list_tempos
    # global ultimo_tempo
    if iotprotocol in pkt:
        pkt.show2()
        # tempo_atual = time.time()
        count = count + 1
        tamanho_total = tamanho_total + sys.getsizeof(pkt)
        tamanho_total_pkt = open("1-nopre_tamanho_total_pkt.txt","w")
        tamanho_total_pkt.write(str(tamanho_total))
        tamanho_total_pkt.write("\n")
        nopre_total_pkt = open("1-nopre_total_pkt.txt","a")
        nopre_total_pkt.write(str(count))
        nopre_total_pkt.write("\n")
        # if (count == 1200):
            
        # elif (count == 100):
        #     nopre_total_pkt = open("nopre_total_pkt.txt","a")
        #     nopre_total_pkt.write(str(count))
        #     nopre_total_pkt.write("\n")
        # elif (count == 200):            
        #     nopre_total_pkt = open("nopre_total_pkt.txt","a")
        #     nopre_total_pkt.write(str(count))
        #     nopre_total_pkt.write("\n")
        # elif (count == 300):
        #     nopre_total_pkt = open("nopre_total_pkt.txt","a")
        #     nopre_total_pkt.write(str(count))
        #     nopre_total_pkt.write("\n")
        # list_tempos.append(tempo_atual - ultimo_tempo)
        # ultimo_tempo = tempo_atual
        # if (count > 1):
        #     median = (statistics.median(list_tempos[1:]))
        #     # Abre o arquivo med_tx_receb_pkt.txt e escreve a media 
        #     # da taxa de recebimento de count pacotes
        #     med_tx_receb_pkt = open("med_tx_receb_pkt.txt","a")
        #     med_tx_receb_pkt.write(str(median))
        #     med_tx_receb_pkt.write("\n")
        

   
    sys.stdout.flush()

        # Criar lista iot_agregado que sera enviado a BC, dar append nos campos
        # iot_agregado = []
        # iot_agregado.append(pkt[iotprotocol].iot_id)
        # iot_agregado.append(pkt[iot_agregacao][0].iot_agg)
        # iot_agregado.append(pkt[iot_agregacao][1].iot_agg)
        # iot_agregado.append(pkt[iot_agregacao][2].iot_agg)

        # Gerar arquivo txt quando nr de pacotes atingir o nr do teste - 100:

            

# Conectar com Ethereum e mandar como transaçoes
# # def sendtoblockchain(iot_agregado):

# # Criar script python com web3

# # txn_hash = counter.functions.envia_pkt_agregado(pkt[iot_agregacao][0],pkt[iot_agregacao][1],pkt[iot_agregacao][2]).transact({"from": me})
# # contrato.funcoes.envia_pkt_agregado(31, 20, 30, 40)

def main():
    ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth' in i]
    iface = ifaces[0]
    print("sniffing on %s" % iface)
    sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
