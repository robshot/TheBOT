from irc import *
import os
import random

channel = "#pythonbottest"
server = "178.118.237.238"
port = 5000
nickname = "TheBOT"

irc = IRC()
irc.connect(server, port, channel, nickname)


while 1:
    text = irc.get_text()
    print text

    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")