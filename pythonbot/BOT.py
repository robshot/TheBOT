#!/usr/bin/env python3

import socket

SERVER = '178.118.237.238'
PORT = 5000
CHANNEL = "#pythonbottest"
BOTNICK = 'TheBOT'
COMMAND_SIGN = '@'

def Send(target, message):
	sock.send(('PRIVMSG '+target+' :'+message+'\r\n').encode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Connecting to server')

sock.connect((SERVER,PORT))
sock.send(('quote PASS TheBOT:Test').encode())
sock.send(('USER '+BOTNICK+' '+BOTNICK+' '+BOTNICK+" :hi.\r\n").encode())
sock.send(('NICK '+BOTNICK + "\r\n").encode())
sock.send(('JOIN '+CHANNEL + "\r\n").encode())

sock.send(('PRIVMSG '+CHANNEL+" :This is a test.\r\n").encode())

print('Server connection succeeded!')

def main():
	print('Main loop')
	while True:
		print("Inside While")
		
   		text = sock.recv(2048)
   		print(text)

	   	if text.find('PING') != -1: 
      			sock.send(('PONG ' + text.split() [1] + '\r\n').encode())	
			
main()
