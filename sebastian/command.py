from enum import Enum
from typing import List

from . import proto

class Command(Enum):
    """
    Commands for Sebastian's movement.
    """

    FORWARD = 'forward'
    LEFT = 'left'
    RIGHT = 'right'

    # STOP = 'stop'

    @staticmethod
    def from_str(cmd: 'str') -> 'Command':
        cmd = cmd.lower()
        switch = {
            'forward': Command.FORWARD,
            'left': Command.LEFT,
            'right': Command.RIGHT,
            # 'stop': Command.STOP,
        }
        return switch[cmd]

    @staticmethod
    def values() -> 'List[Command]':
        return [c.value for c in Command]

    @staticmethod
    def function(cmd: 'str'):
        switch = {
            'forward': proto.Control.forward,
            'left': proto.Control.left,
            'right': proto.Control.right
        }
        return switch[cmd]
