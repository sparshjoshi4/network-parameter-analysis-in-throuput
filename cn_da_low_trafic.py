from scapy.all import *
import time

target = "8.8.8.8"   # Google DNS (safe & reachable)

for i in range(20):  # LOW traffic
    pkt = IP(dst=target)/TCP(dport=80, flags="S")
    send(pkt, verbose=False)
    time.sleep(1)

print("sparsh")