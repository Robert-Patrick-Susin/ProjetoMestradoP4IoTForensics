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

# Envia os pacotes na ordem original que foram criados
#!/usr/bin/python
# from scapy.all import *
# import time, sys
# pkts = rdpcap("../../../Downloads/normal_MQTT_sensors_send_1min.pcap")
# clk = pkts[0].time
# for p in pkts:
#     time.sleep(p.time - clk)
#     clk = p.time
#     sendp(p)


# Envia uma quantidade X de pacotes para testar agregação/filtragem
from scapy.all import rdpcap, sendp

# Replace 'your_file.pcap' with the actual PCAP file path
pcap_file_path = '../../../Downloads/normal_MQTT_sensors_send_1min.pcap'

# Read packets from the PCAP file
packets = rdpcap(pcap_file_path)

# Select a subset of packets to send (e.g., the first 5 packets)
packets_to_send = packets[:8]

# Send selected packets
sendp(packets_to_send)