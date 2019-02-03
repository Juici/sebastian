import os

from dotenv import load_dotenv
from enum import Enum
from typing import List

from .twitch import TwitchBot


class Command(Enum):
    """
    Commands for Sebastian's movement.
    """

    FORWARD = 'forward'
    LEFT = 'left'
    RIGHT = 'right'
    STOP = 'stop'

    @staticmethod
    def from_str(cmd: 'str') -> 'Command':
        cmd = cmd.lower()
        switch = {
            'forward': Command.FORWARD,
            'left': Command.LEFT,
            'right': Command.RIGHT,
            'stop': Command.STOP,
        }
        return switch[cmd]

    @staticmethod
    def values() -> 'List[Command]':
        return [c.value for c in Command]


class Sebastian:
    """
    Sebastian the robot.
    """

    def __init__(self):
        load_dotenv()

        self.bot = TwitchBot(
            self,
            channel=os.environ['TWITCH_CHANNEL'],
            username=os.environ['TWITCH_USERNAME'],
            password=os.environ['TWITCH_PASSWORD'],
            host=os.environ['IRC_HOST'],
            port=os.environ['IRC_PORT'],
        )

    def run(self):
        self.bot.start()

    def handle_command(self, cmd: 'Command'):
        print('handle {}'.format(cmd.value))

        pass
