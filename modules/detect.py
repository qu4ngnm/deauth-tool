from scapy.all import *

# AP MAC address
AP_MAC = "00:11:22:33:44:55"

def deauth_detector(pkt):
    if pkt.haslayer(Dot11Deauth) and pkt.addr1 == AP_MAC:
        print("[X] Deauthentication packet targeting AP detected!")

sniff(prn=deauth_detector)
