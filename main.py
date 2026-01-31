from telethon import TelegramClient, events
from config import API_ID, API_HASH, SESSION
from queue import add_song, get_queue, pop_song
import yt_dlp
import os

client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r"\.play (.+)"))
async def play(event):
    query = event.pattern_match.group(1)

    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "quiet": True
    }

    os.makedirs("downloads", exist_ok=True)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=True)
        file = ydl.prepare_filename(info)

    add_song(event.chat_id, file)
    await event.reply(f"🎶 Added to queue:\n**{info['title']}**")

@client.on(events.NewMessage(pattern=r"\.queue"))
async def queue_cmd(event):
    q = get_queue(event.chat_id)
    if not q:
        return await event.reply("Queue empty")

    msg = "\n".join(f"{i+1}. {s}" for i, s in enumerate(q))
    await event.reply(f"🎧 Queue:\n{msg}")

client.start()
client.run_until_disconnected()
