from scapy.all import *
import time

target = "8.8.8.8"   # Google DNS (safe & reachable)

for i in range(300):   # HEAVY traffic
    pkt = IP(dst=target)/TCP(dport=80, flags="S")
    send(pkt, verbose=False)
    
print("Sparsh")