from telethon import TelegramClient, events
from telethon.sessions import StringSession

from config import API_ID, API_HASH, SESSION
from music_queue import add_song, get_queue

import yt_dlp
import os

# ─── TELETHON CLIENT ──────────────────────────────────────────────
client = TelegramClient(
    StringSession(SESSION),
    API_ID,
    API_HASH
)

# ─── YT-DLP OPTIONS (ANTI-BOT SAFE MODE) ─────────────────────────
YDL_OPTS = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "quiet": True,
    "default_search": "ytsearch",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "ignoreerrors": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

os.makedirs("downloads", exist_ok=True)

# ─── PLAY COMMAND ────────────────────────────────────────────────
@client.on(events.NewMessage(pattern=r"\.play (.+)"))
async def play(event):
    query = event.pattern_match.group(1).strip()

    # text → ytsearch
    if not query.startswith("http"):
        query = f"ytsearch:{query}"

    await event.reply("🔍 Searching & downloading...")

    try:
        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(query, download=True)

            # ytsearch returns entries
            if "entries" in info:
                info = info["entries"][0]

            if not info:
                return await event.reply("❌ No results found.")

            file_path = ydl.prepare_filename(info)

    except Exception as e:
        return await event.reply(f"❌ Download failed:\n`{e}`")

    add_song(event.chat_id, file_path)

    await event.reply(
        f"🎶 **Added to queue**\n"
        f"**Title:** {info.get('title')}\n"
        f"**Duration:** {info.get('duration', 'N/A')} sec"
    )

# ─── QUEUE COMMAND ───────────────────────────────────────────────
@client.on(events.NewMessage(pattern=r"\.queue"))
async def queue_cmd(event):
    q = get_queue(event.chat_id)

    if not q:
        return await event.reply("🎧 Queue is empty.")

    msg = "\n".join(f"{i+1}. {os.path.basename(s)}" for i, s in enumerate(q))
    await event.reply(f"🎧 **Current Queue:**\n{msg}")

# ─── START BOT ───────────────────────────────────────────────────
client.start()
print("✅ Telethon Music Bot Started")
client.run_until_disconnected()
