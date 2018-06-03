#!usr/bin/python2
import socket
import os,commands 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",7777))
for i in range(100) :
	data=s.recvfrom(100)
	check[0]=Commands.getstatusoutput(data[0])
	if check == 0
		s.sendto(check[1],data[1])
	else
	'''
	print data 
	s.sendto("hmmmm",data[1])
	'''
