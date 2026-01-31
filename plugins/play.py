from pyrogram import filters
from musicbot import bot
from utils.yt import yt_search
from utils.spotify_api import spotify_track
from utils.vc import vc
from pytgcalls.types.input_stream import AudioPiped

@bot.on_message(filters.command("play") & filters.group)
async def play(_, m):
    if len(m.command) < 2:
        return await m.reply("🎵 Song name do")

    query = " ".join(m.command[1:])

    if "spotify.com" in query:
        query = spotify_track(query)

    url = yt_search(query)
    await vc.join_group_call(
        m.chat.id,
        AudioPiped(url),
        stream_type="local_stream"
    )
    await m.reply(f"▶️ <b>Playing:</b> {query}")
