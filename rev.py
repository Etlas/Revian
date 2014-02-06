import socket
import random
import urllib

botnick = Rev

def ping():
	pongo = "PONG :Pong\n"
	ircsock.send(pongo.encode('utf-8'))
        
def sendmsg(chan , msg):
	privy = "PRIVMSG "+ chan +" :"+ msg + "\n"
	ircsock.send(privy.encode('utf-8'))

def joinchan(chan):
	joinn = "JOIN "+ chan +"\n"
	ircsock.send(joinn.encode('utf-8'))
        
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using port 6667
test = "USER "+ botnick +" "+ botnick +" "+ botnick +" :Revian bot\n"
ircsock.send(test.encode('utf-8')) # user authentication
test2 = "NICK "+ botnick +"\n"
ircsock.send(test2.encode('utf-8')) # here we actually assign the nick to the bot
test3 = "JOIN #gekinzuku\n"
ircsock.send(test3.encode('utf-8'))


while 1: # Be careful with these! It might send you to an infinite loop
        ircmsg = ircsock.recv(2048).decode('utf-8') # receive data from the server
        ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
        try:
                print(ircmsg) # Here we print what's coming from the server
        except UnicodeEncodeError:
                print('Encode Failed to Print')
        
	if (ircmsg.find("PRIVMSG") != -1): #Translate common message elements into variables
		nicksplit = ircmsg.split('!')
		global nick
		nick = nicksplit[0][1:]
		channelsplit = ircmsg.split(' ')
		global channel
		channel = channelsplit[2]
		msgsplit = ircmsg.split(':')
		global msg
		msg = msgsplit[2]
  
        if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
                ping()
            
        
