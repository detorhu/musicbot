from pyrogram import Client
from pytgcalls import PyTgCalls

from bot.config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING


# Telegram Bot
bot = Client(
    name="MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

# Assistant Account (VC join karega)
assistant = Client(
    name="Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    in_memory=True
)

# PyTgCalls instance
call = PyTgCalls(assistant)
