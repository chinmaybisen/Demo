#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip=""
server_port=9999

while True :
	msg=raw_input("enter your message:")
	s.sendto(msg,(server_ip,server_port))
	print s.recvfrom(100)

