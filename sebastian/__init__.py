"""
Entry point to Sebastian.
"""

from .robot import Robot


def run():
    bot = Robot()
    bot.run()
