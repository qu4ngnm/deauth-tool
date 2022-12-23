# ap_mac = "68:ff:7b:88:07:5c"
#
# from scapy.all import *
#
# def list_clients(ap_mac, interface):
#     client_macs = []
#     def packet_handler(packet):
#         if packet.haslayer(Dot11):
#             # Check if the packet is a management frame and the AP MAC address matches
#             if packet.type == 0 and packet.addr1 == ap_mac:
#                 # Add the client MAC address to the list
#                 client_macs.append(packet.addr2)
#
#     # Start sniffing packets
#     sniff(iface=interface, prn=packet_handler)
#
#     return client_macs
#
#
# ap_mac = "68:ff:7b:88:07:5c"
# interface = "wlp5s0mon"
# clients = list_clients(ap_mac, interface)
# print(clients)

# from scapy.all import *
#
# # Set the interface to monitor mode
# conf.iface = "wlp5s0mon"
#
# # Capture packets transmitted over the wireless network
# packets = sniff(filter="dst host 68:ff:7b:88:07:5c", count=1000)
#
# # Extract the source MAC address of each packet
# clients = set()
# for packet in packets:
#     clients.add(packet.src)
#
# # Print the list of clients
# print(clients)

# from scapy.all import *
#
# # Set the AP's MAC address
# ap_mac = "68:ff:7b:88:07:5c"
#
# # Set the sniffing duration
# duration = 60
#
# # Set the filter to capture packets sent to the AP's MAC address
# filter = "ether dst " + ap_mac
#
# # Set of seen MAC addresses
# seen = set()
#
# def process_packet(packet):
#     # Extract the source MAC address from the packet
#     src_mac = packet[Ether].src
#
#     # Check if the MAC address has been seen before
#     if src_mac not in seen:
#         # Print the MAC address
#         print(src_mac)
#
#         # Add the MAC address to the set of seen addresses
#         seen.add(src_mac)
#
# # Capture packets and pass them to the callback function
# sniff(prn=process_packet, filter=filter, count=100)
# print(seen)

import os
import time

from scapy.all import *
clients = []

def scan_ap(ap_mac):
    # Send probe request
    pkt = RadioTap()/Dot11(type=0, subtype=4, addr1="ff:ff:ff:ff:ff:ff", addr2=ap_mac, addr3=ap_mac)/Dot11ProbeReq()
    sendp(pkt, iface="wlp5s0mon", count=20)

    # Capture probe response
    pkt = sniff(iface="wlp5s0mon", count=1, timeout=2)
    if pkt and pkt[0].haslayer(Dot11ProbeResp):
        return pkt[0][Dot11].addr1
    return None

ap_mac = "68:ff:7b:88:07:5c"  # Replace with the MAC address of the AP

while True:
    client_mac = scan_ap(ap_mac)
    if client_mac and client_mac not in clients:
        clients.append(client_mac)
        print(f"Found client: {client_mac}")
    time.sleep(1)
# # Import the Scapy modules
# from scapy.all import *
#
# # Capture packets on the network
# packets = sniff(iface="wlp5s0mon", filter="ether src 68:ff:7b:88:07:5c")
#
# # Iterate over the packets and print the MAC address of each client
# for packet in packets:
#     client_mac = packet[Ether].src
#     print(client_mac)

# import scapy.all as scapy
# mac_addresses = []
# def get_mac_addresses():
#     # Send an ARP request to the broadcast address
#     arp_request = scapy.Ether(dst="68:ff:7b:88:07:5c")/scapy.ARP(pdst="192.168.1.1/24")
#     responses, _ = scapy.srp(arp_request, iface="wlp5s0mon", timeout=2)
#
#     # Extract the MAC addresses from the responses
#
#     for response in responses:
#         mac_addresses.append(response[1].hwsrc)
#
#     return mac_addresses
#
# print(get_mac_addresses())
# print(mac_addresses)

# import subprocess
#
# def get_connected_stations(ap_mac_address):
#     # Run the airodump-ng command to capture information about the AP
#     proc = subprocess.run(["airodump-ng", "wlp5s0mon", "--bssid", ap_mac_address, "--output-format", "csv"], capture_output=True)
#
#     # Split the output into lines
#     lines = proc.stdout.decode().strip().split("\n")
#
#     # Extract the MAC addresses of the stations from the output
#     mac_addresses = []
#     for line in lines[1:]:
#         fields = line.split(",")
#         if fields[0] != "Station MAC":
#             mac_addresses.append(fields[0])
#
#     return mac_addresses
#
# mac_addresses = get_connected_stations("68:ff:7b:88:07:5c")
# print(mac_addresses)

# from scapy.all import *
#
# # Set up the interface to use for sending and receiving packets
# conf.iface = "wlp5s0mon"
#
# # Create an ARP request packet
# arp_request = Ether(dst="68:ff:7b:88:07:5c")/ARP(pdst="192.168.1.0/24", hwdst="68:ff:7b:88:07:5c")
#
# # Send the packet using sendp()
# sendp(arp_request, verbose=1)
#
# # Wait for the responses and print them
# arp_response = sniff(count=10, filter="arp")
# for response in arp_response:
#     print(response.hwsrc)
