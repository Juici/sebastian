from .rpi import RPi

# Angle per turn command.
TURN_ANGLE = 10


class Robot:
    """
    Sebastian the robot.
    """

    def __init__(self):
        # TODO: initialize twitch stuff
        self.rpi = RPi()

    def run(self):
        # TODO: start twitch hooks

        self.on_command('left')

        import time
        time.sleep(5)

    def on_command(self, cmd):
        switcher = {
            'forward': self.rpi.forward,
            'left': self.rpi.left,
            'right': self.rpi.right,
            'stop': self.rpi.stop
        }
        cmd = str(cmd).lower()
        switcher[cmd]()
