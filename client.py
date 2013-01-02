#!/usr/bin/env python
import socket

port = 8000

def send(text):
	server=socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	server.connect( ('localhost',port) )
	server.send(text)
	data=server.recv(1024)
	server.close()
	return data

def console():
	text = result = ""
	while text != "quit()":
		text = raw_input("Rhino >>> ")
		if text != "":
			result = send(text)
		print result
	
def kill():
	server=socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	server.connect( ('localhost',port) )
	server.shutdown(2)
	server.close()
	
if __name__=="__main__":
	console()