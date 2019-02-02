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

    def on_command(self, cmd):
        switcher = {
            'forward': noop,
            'left': noop,
            'right': noop,
            'stop': noop
        }
        cmd = str(cmd).lower()
        switcher[cmd]()


def noop():
    pass
