from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram.enums import ParseMode

bot = Client(
    "AdvanceeMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML,
    plugins=dict(root="plugins")
)

bot.run()