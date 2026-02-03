from pyrogram import filters
from bot.client import bot
from bot.config import OWNER_ID

@bot.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart(_, msg):
    await msg.reply("♻ Restarting...")
    exit()
