#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5838655940:AAEh36OBWskzA97ZOdBr98390qIHFQ9sGe8")
    API_ID = int(os.environ.get("API_ID", "29540156"))
    API_HASH = os.environ.get("API_HASH", "775d47859519f34f01549344a392280b")
    

