from scapy.all import *
from myIoT_agg_header import *

TYPE_IOTPROTOCOL = 0x1212
TYPE_IPV4 = 0x0800

class iotprotocol(Packet):
    name = "iotprotocol"
    fields_desc = [
        ShortField("iot_id", 0),
        ShortField("iot_leituras", 0),
        ShortField("next_hdr", 0)
    ]
    def mysummary(self):
        return self.sprintf("iot_id=%iot_id%, iot_reads=%iot_leituras%")


bind_layers(Ether, iotprotocol, type=TYPE_IOTPROTOCOL)
bind_layers(iotprotocol, iot_agregacao, next_hdr=1)
bind_layers(iotprotocol, IP, next_hdr=0)

