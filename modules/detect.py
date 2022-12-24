from scapy.all import *
from scapy.layers.dot11 import Dot11Deauth
from termcolor import colored
import time

count = 0
def sniffer(pkt):
    global count
    if pkt.haslayer(Dot11Deauth):
        count += 1
        if count > 100:
            print(colored(("[X] Deauthentication frame from {} to {}".format(pkt.addr2, pkt.addr1)), color="red"))
            time.sleep(2)

sniff(iface="wlp5s0mon", prn=sniffer)