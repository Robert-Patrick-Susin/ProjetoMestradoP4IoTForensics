from scapy.all import *
from myIoT_header import *

TYPE_IPV4 = 0x800

class iot_agregacao(Packet):
    name = "iot_agregacao"
    fields_desc = [
        ShortField("iot_agg", 0),
        ShortField("next_hdr", 0),
    ]
    def mysummary(self):
        return self.sprintf("iot_agg=%iot_agg%, next_hdr=%next_hdr%")

bind_layers(iot_agregacao, iot_agregacao, next_hdr=1)
bind_layers(iot_agregacao, IP, next_hdr=0)