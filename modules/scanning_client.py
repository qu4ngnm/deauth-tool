# ap_mac = "68:ff:7b:88:07:5c"

# from scapy.all import *

# def list_clients(ap_mac, interface):
#     client_macs = []
#     def packet_handler(packet):
#         if packet.haslayer(Dot11):
#             # Check if the packet is a management frame and the AP MAC address matches
#             if packet.type == 0 and packet.addr1 == ap_mac:
#                 # Add the client MAC address to the list
#                 client_macs.append(packet.addr2)
    
#     # Start sniffing packets
#     sniff(iface=interface, prn=packet_handler)
    
#     return client_macs


# ap_mac = "68:ff:7b:88:07:5c"
# interface = "wlp5s0mon"
# clients = list_clients(ap_mac, interface)
# print(clients)

# from scapy.all import *

# # Set the interface to monitor mode
# conf.iface = "wlp5s0mon"

# # Capture packets transmitted over the wireless network
# packets = sniff(filter="dst host 68:ff:7b:88:07:5c", count=1000)

# # Extract the source MAC address of each packet
# clients = set()
# for packet in packets:
#     clients.add(packet.src)

# # Print the list of clients
# print(clients)

# from scapy.all import *

# # Set the AP's MAC address
# ap_mac = "68:ff:7b:88:07:5c"

# # Set the sniffing duration
# duration = 60

# # Set the filter to capture packets sent to the AP's MAC address
# filter = "ether dst " + ap_mac

# # Set of seen MAC addresses
# seen = set()

# def process_packet(packet):
#     # Extract the source MAC address from the packet
#     src_mac = packet[Ether].src
    
#     # Check if the MAC address has been seen before
#     if src_mac not in seen:
#         # Print the MAC address
#         print(src_mac)
        
#         # Add the MAC address to the set of seen addresses
#         seen.add(src_mac)

# # Capture packets and pass them to the callback function
# sniff(prn=process_packet, filter=filter, count=100)


import os
import time

from scapy.all import *

# Set interface to monitor mode
# os.system("ifconfig wlan0 down")
# os.system("iwconfig wlan0 mode monitor")
# os.system("ifconfig wlan0 up")

def scan_ap(ap_mac):
    # Send probe request
    pkt = RadioTap()/Dot11(type=0, subtype=4, addr1="ff:ff:ff:ff:ff:ff", addr2=ap_mac, addr3=ap_mac)/Dot11ProbeReq()
    sendp(pkt, iface="wlan0")

    # Capture probe response
    pkt = sniff(iface="wlan0", count=1, timeout=2)
    if pkt and pkt[0].haslayer(Dot11ProbeResp):
        return pkt[0][Dot11].addr2
    return None

ap_mac = "aa:bb:cc:dd:ee:ff"  # Replace with the MAC address of the AP

while True:
    client_mac = scan_ap(ap_mac)
    if client_mac and client_mac not in clients:
        clients.append(client_mac)
        print(f"Found client: {client_mac}")
    time.sleep(1)
