#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6762429127:AAGtoXU_FhnqaXjAVG_s5Fh9VJktu2ry6Zc")
    API_ID = int(os.environ.get("API_ID", "29540156"))
    API_HASH = os.environ.get("API_HASH", "775d47859519f34f01549344a392280b")
    AUTH_USERS = 1476002847

