#!/usr/bin/env python3

import irc.bot
import threading

from voting import Voting

# Stolen from
# https://github.com/jaraco/irc/blob/master/scripts/testbot.py
class Bot(irc.bot.SingleServerIRCBot):

    def __init__(self, channel, nickname, server, password, port=6667):
        print(port)
        irc.bot.SingleServerIRCBot.__init__(
            self,
            [(server, port, password)],
            nickname,
            nickname
        )
        self.channel = channel
        # Set the state of the robot.
        self.state = {
            'left': 0,
            'right': 0
        }
        # Current scores.
        self.scores = Voting(['forward', 'stop', 'left', 'right'])

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + '_')

    def on_welcome(self, c, e):
        c.join(self.channel)
        print('JOINED')
        Bot.count(c, self.channel, self.scores)

    def on_pubmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_privmsg(self, c, e):
        print(e)

    # Handle the voting here.
    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection
        if cmd[0] == '!' and len(cmd) > 1:
            res = self.scores.vote(cmd[1:])
            if not res:
                c.privmsg(self.channel, '@{},  Invalid option!'.format(nick))

    @staticmethod
    def count(c, channel, scores):
        # Loop self
        threading.Timer(10.0, Bot.count, args=[c, channel, scores]).start()
        res = scores.result()
        scores.clear()
        if res is not None:
            c.privmsg(channel, "DECIDED ON: {}".format(res))
            # Send action to backend now
            pass

