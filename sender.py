#!usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(100) :
	msg=raw_input("enter your message : ")
	s.sendto(msg,("127.0.0.1",7777))
	print s.recvfrom(100)

