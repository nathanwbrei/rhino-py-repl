#!/usr/bin/env python
import socket
import code
import sys

port = 8000

def run_server():

	class Toasty_buffer:
		def __init__(self):
			self.content = []
		def write(self, string):
			self.content.append(string)

	print "Server started..."

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', port))
	s.listen(1)

	buf = Toasty_buffer()
	sys.stdout = sys.stderr = buf

	cmd = ''
	intr = code.InteractiveConsole()

	while cmd != 'quit()':
	
		conn, addr = s.accept()
		cmd = conn.recv(1024)

		multiline = intr.push(cmd)
		if multiline:
			buf.write('...')
	
		sockfile = conn.makefile('w', 5000)
		sockfile.writelines(buf.content)
		sockfile.close()
		conn.close()
		buf.__init__()
	
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__
#	conn.shutdown(0)
#	conn.close()
	
if __name__=="__main__":
	run_server()