<<<<<<< HEAD
#!/usr/bin/env python3

import socket

#SERVER = 'irc.freenode.net'
SERVER = 'irc.quakenet.org'
#SERVER = '178.118.237.238'
#PORT = 5000
PORT = 6667
CHANNEL = "#pythonbottest2"
BOTNICK = 'TheBOT2'
COMMAND_SIGN = '@'

def Send(target, message):
	sock.send(('PRIVMSG '+target+' :'+message+'\r\n').encode())
#	print(message)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Connecting to server')
sock.connect((SERVER,PORT))
#sock.send(('quote PASS TheBOT:Test').encode())
sock.send(('USER '+BOTNICK+' '+BOTNICK+' '+BOTNICK+" :hi.\r\n").encode())
sock.send(('NICK '+BOTNICK + "\r\n").encode())
#sock.send(('JOIN '+CHANNEL + "\r\n").encode())
#sock.send(('PRIVMSG '+CHANNEL+" :This is a test.\r\n").encode())
print('Server connection succeeded!')

def main():
	print('Main loop')
	import time
	time.sleep(5)
	sock.send(('JOIN ' + CHANNEL + "\r\n").encode()) 
	while True:
		print('Main loop while')
#		sock.send('Testje')
#		Send(CHANNEL,'Test')
		received = sock.recv(2048).decode('latin1')
		print(received)
#		received = received[:len(received)-len('\r\n')]
#		print(received)
#		Send(CHANNEL,'Testje')
		import time
		time.sleep(5)		
#		print('Listening...')
#   		text = sock.recv(2048).decode('UTF-8')
#   		print(text)   #print text to console

#	   	if text.find('PING') != -1:                          #check if 'PING' is found
#      			sock.send(('PONG ' + text.split() [1] + '\r\n').encode()) #returnes 'PONG' back to the server (prevents pinging out!)	
			
#Shenanigans.
				
#		if received.find(COMMAND_SIGN+'test') != -1:
#			try:
#				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Yes, I am working. You idiot...')
#				import time
#				time.sleep(5)
#			except:
#				continue					
#if __name__ == "__main__":
#	main()

