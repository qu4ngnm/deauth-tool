from scapy.all import *

# AP MAC address
AP_MAC = "00:11:22:33:44:55"

def deauth_detector(pkt):
    if pkt.haslayer(Dot11Deauth) and pkt.addr1 == AP_MAC:
        print("[X] Deauthentication packet targeting AP detected!")

sniff(prn=deauth_detector)

# from scapy.layers.dot11 import Dot11Deauth

# # Set up the packet sniffer
# def sniffer(pkt):
#     # Check if the packet is a deauthentication frame
#     if pkt.haslayer(Dot11Deauth):
#         # Print the MAC addresses of the sender and receiver
#         print("Deauthentication frame from {} to {}".format(pkt.addr2, pkt.addr1))

# # Start the packet sniffer
# sniff(iface="wlan0", prn=sniffer)
