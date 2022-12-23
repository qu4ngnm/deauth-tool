from scapy.all import *
from scapy.layers.dot11 import Dot11Deauth
from termcolor import colored

def sniffer(pkt):
    count = 0
    if pkt.haslayer(Dot11Deauth):
        count += 1
        if count > 20:
            print(colored(("[X] Deauthentication frame from {} to {}".format(pkt.addr2, pkt.addr1)), color="red"))

sniff(iface="wlp5s0mon", prn=sniffer)