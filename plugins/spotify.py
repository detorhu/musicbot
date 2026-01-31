from pyrogram import filters
from mysicbot import bot
from utils.spotify_api import spotify_track
from utils.yt import yt_search
from utils.queue import add_song


@bot.on_message(filters.command("spotify") & filters.group)
async def spotify_play(_, m):
    if len(m.command) < 2:
        return await m.reply("🎧 Spotify link ya song name do")

    query = " ".join(m.command[1:])
    yt_query = spotify_track(query)
    url = yt_search(yt_query)

    song = {
        "title": yt_query,
        "url": url,
        "requested_by": m.from_user.id
    }

    add_song(m.chat.id, song)
    await m.reply(f"🎵 Spotify se add kiya: <b>{yt_query}</b>")
