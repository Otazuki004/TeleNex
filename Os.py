#Setup Process

import os
from pyrogram import *
from datetime import *

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
