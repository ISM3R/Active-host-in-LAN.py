#!/usr/bin/env python3

import subprocess 
import os

ip = str(input("Enter address to scan [default: 192.168.1.0]: ") or "192.168.1.0")
ip = ip.split('.')[0] + "." + ip.split('.')[1] + "." + ip.split('.')[2] + "."
from_host = int(input("Starting from host [default: 0]: ") or "0")
to_host = int(input("To host [default: 256]: ") or "256")
interface = str(input("Interface: "))
thread = str(input("Number of thread [default: 3]") or "3")
FNULL = open(os.devnull, 'w')

for ping in range(from_host, to_host):
    address = ip.split('.')[0]+"."+ip.split('.')[1]+"."+ip.split('.')[2]+"." + str(ping)
    res = subprocess.call(['ping', '-I', interface, '-c', thread, address], stdout=FNULL, stderr=subprocess.STDOUT)
    if res == 0: 
        print( "ping to", address, "OK") 
    elif res == 2: 
        print("no response from", address) 
    else: 
        print("ping to", address, "failed!")
