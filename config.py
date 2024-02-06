#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6223962185:AAHs4HFFTWI5HKcX2CLbluDaVYO54SOkHNI")
    API_ID = int(os.environ.get("API_ID", "20012414"))
    API_HASH = os.environ.get("API_HASH", "7ce06c4eee35a4832e0adae83afe89df)
    AUTH_USERS = 5656436152

