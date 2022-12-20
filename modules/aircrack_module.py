import subprocess
import time

def enable_monitor_mode(interface):
    kill_process = subprocess.Popen(['sudo','airmon-ng', 'check', 'kill'])
    res = subprocess.Popen(['sudo','airmon-ng', 'start', interface])
    exit(0)

def enable_managed_mode(interface):
    res = subprocess.Popen(['airmon-ng', 'stop', interface])
    restart_network = subprocess.Popen(['service', 'NetworkManager','start'])
    exit(0)

def find_wifi(interface):
    airodump = subprocess.Popen(['airodump-ng', interface])
    time.sleep(8)
    exit(0)


# enable_monitor_mode('wlp5s0')
# enable_managed_mode('wlp5s0mon')