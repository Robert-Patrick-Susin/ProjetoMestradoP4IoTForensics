from scapy.all import *

sendp(rdpcap("../../../Downloads/normal_MQTT_sensors_send_1min.pcap"))