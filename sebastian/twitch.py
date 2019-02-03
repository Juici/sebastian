import threading
import weakref
import irc.bot

from .voting import Voting
from .command import Command

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .robot import Sebastian


# Based on:
# https://github.com/jaraco/irc/blob/master/scripts/testbot.py
class TwitchBot(irc.bot.SingleServerIRCBot):

    def __init__(self, sebastian: 'Sebastian', channel: 'str', username: 'str', password: 'str',
                 host: 'str',
                 port: 'int' = 6667):
        irc.bot.SingleServerIRCBot.__init__(
            self,
            [(host, port, password)],
            username,
            username,
        )
        self.sebastian = weakref.ref(sebastian)
        self.channel = channel
        # Current scores.
        self.scores = Voting(Command.values())

    # noinspection PyMethodMayBeStatic
    def on_nicknameinuse(self, _c, _e):
        self.connection.nick(self.connection.get_nickname() + '_')

    def on_welcome(self, _c, _e):
        self.connection.join(self.channel)
        print('JOINED')
        self.connection.privmsg(self.channel, '[!] bot arrived')
        self.count()

    def on_pubmsg(self, _c, e):
        self.do_command(e, e.arguments[0])

    def do_command(self, e, cmd: 'str'):
        """
        Handle voting logic.
        """
        nick = e.source.nick
        if cmd[0] == '!' and len(cmd) > 1:
            cmda = cmd[1:].lower()
            if cmda[0] == 'l':
                cmda = 'left'
            elif cmda[0] == 'r':
                cmda = 'right'
            elif cmda[0] == 'f':
                cmda = 'forward' 
            res = self.scores.vote(cmda)
            if not res:
                self.connection.privmsg(self.channel, '@{},  Invalid option!'.format(nick))

    def count(self):
        # Loop self
        threading.Timer(3.0, self.count).start()

        res = self.scores.result()
        self.scores.clear()

        if res is not None:
            self.connection.privmsg(self.channel, "DECIDED ON: {}".format(res))

            cmd = Command.from_str(res)

            sebastian = self.sebastian()
            if sebastian is not None:
                sebastian.handle_command(cmd)
