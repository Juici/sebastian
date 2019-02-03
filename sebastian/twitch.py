import threading
import irc.bot

from .voting import Voting


# Based on:
# https://github.com/jaraco/irc/blob/master/scripts/testbot.py
class TwitchBot(irc.bot.SingleServerIRCBot):

    def __init__(self, channel, nickname, server, password, port=6667):
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

    def on_nicknameinuse(self, c, _e):
        c.nick(c.get_nickname() + '_')

    def on_welcome(self, c, _e):
        c.join(self.channel)
        print('JOINED')
        self.count(c, self.channel, self.scores)

    def on_pubmsg(self, _c, e):
        self.do_command(e, e.arguments[0])

    # Handle the voting here.
    def do_command(self, e, cmd: 'str'):
        nick = e.source.nick
        if cmd[0] == '!' and len(cmd) > 1:
            cmd = cmd[1:].lower()
            res = self.scores.vote(cmd)
            if not res:
                self.connection.privmsg(self.channel, '@{},  Invalid option!'.format(nick))

    def count(self, c, channel, scores):
        # Loop self
        threading.Timer(10.0, self.count, args=[c, channel, scores]).start()
        res = scores.result()
        scores.clear()
        if res is not None:
            c.privmsg(channel, "DECIDED ON: {}".format(res))

            # Send action to backend now
            pass
