#!/usr/bin/env python3
import argparse
import random
import socket
import time

from myIoT_header import iotprotocol
from scapy.all import IP, TCP, Ether, get_if_hwaddr, get_if_list, sendp, sendpfast

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip_addr', type=str, help="The destination IP address to use")
    parser.add_argument('message', type=str, help="The message to include in packet")
    #parser.add_argument('--dst_id', type=int, default=None, help='The myTunnel dst_id to use, if unspecified then myTunnel header will not be included in packet')
    args = parser.parse_args()

    addr = socket.gethostbyname(args.ip_addr)
    #dst_id = args.dst_id
    iface = get_if()

    # if (dst_id is not None):
    #     print("sending on interface {} to dst_id {}".format(iface, str(dst_id)))
    #     pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    #     pkt = pkt / MyTunnel(dst_id=dst_id) / IP(dst=addr) / args.message
    # else:
    print("sending on interface {} to IP addr {}".format(iface, str(addr)))
    pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    # ID 1 sensível
    pkt = pkt / iotprotocol(iot_id=1, iot_leituras=3) / IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / args.message

    pkt.show2()
#    hexdump(pkt)
#    print "len(pkt) = ", len(pkt)
    
    # for x in range(0, 9):
    #     global x
    #     x = x + 1

#Enviar pacotes por somente 20 segundos
#inter = 1 (1 pkt por seg)
#inter = 0.462 (Aprox 2 pkt por seg) || 1./2)
#inter = 0.2886 (Aprox 3 pkt por seg) || 1./3)
    # tempo_max = int(20)
    # tempo_inicial = time.time()
    # while (time.time() - tempo_inicial) < tempo_max:
        # sendp(pkt, iface=iface, verbose=False, inter=0.2886)
    sendpfast(pkt, iface=iface, pps=5, loop=10000)
    


if __name__ == '__main__':
    main()