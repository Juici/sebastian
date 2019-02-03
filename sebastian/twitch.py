import threading
import irc.bot

from .voting import Voting
from .robot import Command


# Based on:
# https://github.com/jaraco/irc/blob/master/scripts/testbot.py
class TwitchBot(irc.bot.SingleServerIRCBot):

    def __init__(self, channel: 'str', nickname: 'str', host: 'str', password: 'str',
                 port: 'int' = 6667):
        super(TwitchBot, self).__init__(
            self,
            [(host, port, password)],
            nickname,
            nickname
        )
        self.channel = channel
        # Current scores.
        self.scores = Voting(Command.values())

    # noinspection PyMethodMayBeStatic
    def on_nicknameinuse(self, _c, _e):
        self.connection.nick(self.connection.get_nickname() + '_')

    def on_welcome(self, _c, _e):
        self.connection.join(self.channel)
        print('JOINED')
        self.count()

    def on_pubmsg(self, _c, e):
        self.do_command(e, e.arguments[0])

    def do_command(self, e, cmd: 'str'):
        """
        Handle voting logic.
        """
        nick = e.source.nick
        if cmd[0] == '!' and len(cmd) > 1:
            cmd = cmd[1:].lower()
            res = self.scores.vote(cmd)
            if not res:
                self.connection.privmsg(self.channel, '@{},  Invalid option!'.format(nick))

    def count(self):
        # Loop self
        threading.Timer(10.0, self.count).start()
        res = self.scores.result()
        self.scores.clear()
        if res is not None:
            self.connection.privmsg(self.channel, "DECIDED ON: {}".format(res))

            # Send action to backend now
            pass
