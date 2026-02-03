from pyrogram import filters
from bot.client import bot, call

@bot.on_message(filters.command("stop") & filters.group)
async def stop(_, msg):
    await call.leave_group_call(msg.chat.id)
    await msg.reply("⏹ Music stopped")
