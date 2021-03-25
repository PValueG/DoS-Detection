from scapy.all import *
import socket
import struct
import datetime

def dosDetect():
# This will open up the socket libaries to access the packets
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)

    ipArray = []  #these two lines cretae arrays which can store the ip addresses that are hitting the network
    uniqueArray = []
    
#the next four lines create a text file to track the ips that are hitting the network via the above arrays, wit
    file_txt = open("attack_DoS.txt", 'w')  
    t1 = str(datetime.now())
    file_txt.writelines(t1)
    file_txt.writelines("\n")


    countIP = 0 #this line counts the ips in a global variable
    while True:
        pkt = s.recvfrom(2048)  # This is the standard port that networks and computers use
        ipheader = pkt[0][14:34]
        ip_hdr = struct.unpack("!8sB3s4s4s", ipheader) #converts ip address from binary to string 
        IP = socket.inet_ntoa(ip_hdr[3])
        ipArray.append(IP)
        if IP not in uniqueArray: #checks whether the ip has been tracked before
            uniqueArray.append(IP)
            countIP = countIP + 1 #counts certain ips, if one of them is hit more than 15 times its a DoS attack
            print("count: ", countIP)
        
        print("IP source = :", IP)
        
        if (countIP >= 15 and IP != "10.0.2.1"):
            
            break

    consecHit = 0
    for i in range(1, len(ipARrray)):
        #
        if(ipArray[i] == ipArray[i - 1]) and (ipARrray[i] != "10.0.2.1"):
            consecHit = consecHit + 1

            print("in here", ipARrray[i], end=" ")
    
    if consecHit > 10:
        line = "\n\n15 ip hits: ", "\n", "IP Adreess: ", IP, "\n", "At time: ", t1, "\n"
        file_txt.writelines(line)
        line = "DDOS attack is Detected: \n"
        file_txt.writelines(line)
        line = "IP Address: "
        file_txt.writelines(line)
        file_txt.writelines(IP)
        file_txt.writelines("\n")