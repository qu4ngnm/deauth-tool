import argparse

banner = """

██████╗ ███████╗     █████╗ ██╗   ██╗████████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔════╝    ██╔══██╗██║   ██║╚══██╔══╝██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║  ██║█████╗█████╗███████║██║   ██║   ██║   ███████║       ██║   ██║   ██║██║   ██║██║     
██║  ██║██╔══╝╚════╝██╔══██║██║   ██║   ██║   ██╔══██║       ██║   ██║   ██║██║   ██║██║     
██████╔╝███████╗    ██║  ██║╚██████╔╝   ██║   ██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                             
Group 162 - Research De-authentication attack & PoC
Group members: Tran Thi Thanh - Team leader👩‍💻
               Nguyen Minh Quang
\nHappy Hecking :))
"""

parser = argparse.ArgumentParser(prog='deauth', description='This tool for send de-auth package to perfomr de-authentication attack on wireless devices')
parser.add_argument('-d', dest='daemon_mode', action='store', help='run program in deamon mode')
parser.add_argument('-l', dest='wifi_list', action='store', help='get the wifi list hostpot list with Mac Address')
parser.add_argument('-m', dest='deauth_targets_list', action='store',nargs='+', help='send deauth package to target MAC address')

args = parser.parse_args()
print(banner)