from enum import Enum


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


class Robot:
    """
    Sebastian the robot.
    """

    def __init__(self):
        # TODO: initialize twitch stuff
        pass

    def run(self):
        # TODO: start twitch hooks
        pass

    def handle_command(self, cmd: 'Command'):
        pass
