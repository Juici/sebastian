from enum import Enum
from typing import List


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
