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

# Envia os pacotes na ordem original que foram criados e com delay para não crashar endhost e envia a quantia que eu quero
# from scapy.all import *
# import time, sys
# packets = rdpcap("../../../Downloads/normal_MQTT_sensors_send.pcap")
# packets_to_send = packets[:1000]
# delay_between_packets = 1
# # Delay artificialmente introduzido para o endhost conseguir absorver os pacotes sem dropar
# clk = packets_to_send[0].time
# for p in packets_to_send:
#     time.sleep(p.time - clk)
#     clk = p.time
#     sendp(p)
#     tempo_atual_envio = time.time()
#     time.sleep(delay_between_packets)

# # Envia os pacotes na ordem original que foram criados durante o tempo que eu quero
# from scapy.all import *
# import time, sys

# # Set the duration in minutes
# duration_minutes = 5

# # Calculate the end time
# end_time = time.time() + duration_minutes * 60

# pkts = rdpcap("../../../Downloads/normal_MQTT_sensors_send.pcap")
# # clk = pkts[0].time
# for p in pkts:
#     # time.sleep(p.time - clk)
#     # clk = p.time
#     while time.time() < end_time:
#         sendp(p)

# Envia os pacotes na ordem original que foram criados sem delay e envia a quantia que eu quero
from scapy.all import *
import time, sys
packets = rdpcap("../../../Downloads/normal_MQTT_sensors_send_1min.pcap")
packets_to_send = packets[:400]
# Delay artificialmente introduzido para o endhost conseguir absorver os pacotes sem dropar
clk = packets_to_send[0].time
for p in packets_to_send:
    time.sleep(p.time - clk)
    clk = p.time
    sendp(p)
    