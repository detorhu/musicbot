from telethon import TelegramClient, events
from telethon.sessions import StringSession

from config import API_ID, API_HASH, SESSION
from music_queue import add_song, get_queue

import yt_dlp
import os

# --- Telethon Client with StringSession ---
client = TelegramClient(
    StringSession(SESSION),
    API_ID,
    API_HASH
)

# --- PLAY COMMAND ---
@client.on(events.NewMessage(pattern=r"\.play (.+)"))
async def play(event):
    query = event.pattern_match.group(1)

    if not query.startswith("http"):
        query = f"ytsearch1:{query}"

    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "quiet": True
    }

    os.makedirs("downloads", exist_ok=True)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=True)

        if "entries" in info:
            info = info["entries"][0]

        file = ydl.prepare_filename(info)

    add_song(event.chat_id, file)
    await event.reply(f"🎶 Added to queue:\n**{info['title']}**")
# --- QUEUE COMMAND ---
@client.on(events.NewMessage(pattern=r"\.queue"))
async def queue_cmd(event):
    q = get_queue(event.chat_id)
    if not q:
        return await event.reply("Queue empty")

    msg = "\n".join(f"{i+1}. {s}" for i, s in enumerate(q))
    await event.reply(f"🎧 Queue:\n{msg}")

# --- START ---
client.start()
client.run_until_disconnected()
