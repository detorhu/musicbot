from pyrogram import filters
from bot.client import bot
from bot.utils.yt import get_audio
from bot.player.stream import play_stream
from bot.database.queue_db import add_song

@bot.on_message(filters.command("play") & filters.group)
async def play(_, msg):
    if len(msg.command) < 2:
        return await msg.reply("❌ Song name do")

    query = msg.text.split(None, 1)[1]
    url, title = get_audio(query)

    add_song(msg.chat.id, {"title": title, "url": url})
    await play_stream(msg.chat.id, url)

    await msg.reply(f"🎵 Playing: **{title}**")
