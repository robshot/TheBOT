#!/usr/bin/env python3

import socket

#SERVER = 'irc.freenode.net'
#SERVER = 'irc.quakenet.org'
SERVER = '178.118.237.238'
PORT = 5000
CHANNEL = "#pythonbottest"
BOTNICK = 'TheBOT'
COMMAND_SIGN = '@'

def Send(target, message):
	sock.send(('PRIVMSG '+target+' :'+message+'\r\n').encode())
#	print(message)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect((SERVER,6667))
sock.connect((SERVER,PORT))
sock.send(('quote PASS TheBOT:Test').encode())
sock.send(('USER '+BOTNICK+' '+BOTNICK+' '+BOTNICK+" :hi.\r\n").encode())
sock.send(('NICK '+BOTNICK + "\r\n").encode())
sock.send(('JOIN '+CHANNEL + "\r\n").encode())

def main():
	while True:
		Send(CHANNEL,'Test')
#		received = sock.recv(2048).decode('latin1')
#		received = received[:len(received)-len('\r\n')]
#		print(received)
		Send(CHANNEL,'Testje')
		import time
		time.sleep(5)		
					
				
#Shenanigans.
				
#		if received.find(COMMAND_SIGN+'test') != -1:
#			try:
#				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Yes, I am working. You idiot...')
#				import time
#				time.sleep(5)
#			except:
#				continue					
if __name__ == "__main__":
	main()
