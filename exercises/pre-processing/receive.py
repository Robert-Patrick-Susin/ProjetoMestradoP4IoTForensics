#!/usr/bin/env python3
import os
import sys
import time
import statistics

from myIoT_header import iotprotocol
from myIoT_agg_header import iot_agregacao
from scapy.all import TCP, get_if_list, sniff

ultimo_tempo = time.time()
# Começo do experimento. Quando inicia o receptor
count = 0
tamanho_total = 0
list_tempos = []

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
    # global tamanho_total
    global tempo_atual
    global ultimo_tempo
    
    #Teste para ver se está ok
    if iot_agregacao in pkt:
        pkt.show2()
        count = count + 1
        countbla = open("teste.txt","a")
        countbla.write(str(count))
        countbla.write("\n")
    
    # IF iotprotocol usado para quando há somente filtragem
    # if iotprotocol in pkt:
    #if iot_agregacao in pkt:
    #    pkt.show2()
        #count = count + 1
        # nopre_total_pkt = open("3-pre_agreg_filt_total_pkt.txt","a")
        # nopre_total_pkt.write(str(count))
        # nopre_total_pkt.write("\n")
        # tamanho_total = tamanho_total + sys.getsizeof(pkt)
        # tamanho_total_pkt = open("3-pre_agreg_filt_tamanho_total_pkt.txt","a")
        # tamanho_total_pkt.write(str(tamanho_total))
        # tamanho_total_pkt.write("\n")
        #tempo_atual = time.time()
        #list_tempos.append(tempo_atual - ultimo_tempo)
        #ultimo_tempo = tempo_atual
        #if (count > 1):
        #    median = (statistics.median(list_tempos[1:]))
            # Abre o arquivo 4-pre_med_rec_pkt.txt e escreve a media 
            # da taxa de recebimento de count pacotes
        #    pre_med_rec_pkt = open("metricas/4-pre_med_rec_pkt.txt","w")
        #    pre_med_rec_pkt.write(str(median))
        #    pre_med_rec_pkt.write("\n")
        #    pre_med_rec_pkt.write(str(count))
        
sys.stdout.flush()
def main():
    ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth' in i]
    iface = ifaces[0]
    print("sniffing on %s" % iface)
    sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
