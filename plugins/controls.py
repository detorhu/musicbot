from pyrogram import filters
from bot import bot
from utils.vc import vc

@bot.on_message(filters.command("pause"))
async def pause(_, m):
    await vc.pause_stream(m.chat.id)
    await m.reply("⏸ Paused")

@bot.on_message(filters.command("resume"))
async def resume(_, m):
    await vc.resume_stream(m.chat.id)
    await m.reply("▶️ Resumed")

@bot.on_message(filters.command("stop"))
async def stop(_, m):
    await vc.leave_group_call(m.chat.id)
    await m.reply("⏹ Stopped")