from pyrogram import Client
from pytgcalls import PyTgCalls
from bot.config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING

bot = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

assistant = Client(
    "Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

call = PyTgCalls(assistant)
