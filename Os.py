import os
from datetime import *
from telethon.sync import TelegramClient, events
from telethon import *
from aiogram

try:
    DIR = f"{os.getcwd()}/"
    print("Running On ", DIR)
except Exception as l:
    print("ERROR", l)
    
try:
    bot_token = TOKEN
    api_id = a_id
    api_hash = a_hash
except Exception as e:
	print("Somthing Went Wrong Getting ENV")
	print(" ")
	print(e)

#Telethon Client
Nex = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)
#AioGram Client
TeleNex = None

@Nex.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! I am your bot.')

@Nex.on(events.NewMessage(pattern='/echo'))
async def echo(event):
    await event.respond(event.text)
    exit()

Nex.run_until_disconnected()
