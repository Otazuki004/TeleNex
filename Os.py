#Setup Process

import os
from pyrogram import *
from datetime import *
try:
    DIR = f"{os.getcwd()}/"
    print("Running On ", DIR)
except Exception as l:
    print("ERROR", l)
    
try:
    with open(f"{DIR}token.txt", "r") as f:
        TOKEN = f.read()
    with open(f"{DIR}id.txt", "r") as g:
        API_ID = g.read()
    with open(f"{DIR}hash.txt", "r") as h:
        API_HASH = h.read()
    with open(f"{DIR}own.txt", "r") as j:
        OWN = j.read()
    print("Success Got Bot Env")
  
except Exception as e:
    print("Error", e)

Nex = Client("TeleNex", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH)

@Nex.on_message(filters.command("start")
def start (Nex, message):
    message.reply_text("Hello I am TeleNex")
