import os

from dotenv import load_dotenv

from .twitch import TwitchBot

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .command import Command


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
