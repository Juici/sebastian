#!/usr/bin/env python3

import os

from dotenv import load_dotenv
import bot

load_dotenv()

if __name__ == "__main__":
    # Nickname
    nickname = os.environ['BOT_USERNAME']
    channel = os.environ['CHANNEL_NAME']
    password = os.environ['BOT_PASSWORD']
    host = os.environ['IRC_HOST']
    port = int(os.environ['IRC_PORT'])
    print(nickname, channel, password, host, port)
    twitch = bot.Bot(channel, nickname, host, password, port)
    twitch.start()
