# Teste para editar cabeçalhos dos pacotes
# from scapy.all import *
# from pprint import pprint
# pkts = PcapReader("../../../Downloads/normal_MQTT_sensors_send_1min.pcap") #should be in wireshark-tcpdump format


# p_out = []

# for pkt in pkts:
#     new_pkt = pkt

#     try:
#         new_pkt[Ethernet].dst = "08:00:00:00:41:41"
#         new_pkt[IP].src = "10.0.1.1"
#         new_pkt[IP].dst = "10.0.41.41"
#         del (new_pkt[IP].chksum)
#         del (new_pkt[TCP].chksum)
#     except:
#         pass

#     # pprint(new_pkt.show())
#     p_out.append(new_pkt)
# sendp(PacketList(p_out), iface="eth0")

# Envia os pacotes na ordem original que foram criados e envia a quantia que eu quero
from scapy.all import *
import time, sys
packets = rdpcap("../../../Downloads/normal_MQTT_sensors_send_1min.pcap")
packets_to_send = packets[:200]
clk = packets_to_send[0].time
for p in packets_to_send:
    time.sleep(p.time - clk)
    clk = p.time
    sendp(p)