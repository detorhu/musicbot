from pyrogram import filters
from bot import bot
from utils.database import playlists
from utils.yt import yt_search


@bot.on_message(filters.command("save"))
async def save_song(_, m):
    if len(m.command) < 2:
        return await m.reply("🎵 Song name do")

    query = " ".join(m.command[1:])
    url = yt_search(query)

    playlists.update_one(
        {"user_id": m.from_user.id},
        {"$push": {"songs": {"title": query, "url": url}}},
        upsert=True
    )
    await m.reply("✅ Playlist me save ho gaya")


@bot.on_message(filters.command("myplaylist"))
async def my_playlist(_, m):
    data = playlists.find_one({"user_id": m.from_user.id})
    if not data or not data.get("songs"):
        return await m.reply("📭 Playlist empty hai")

    text = "🎶 <b>Your Playlist</b>\n\n"
    for i, s in enumerate(data["songs"], 1):
        text += f"{i}. {s['title']}\n"

    await m.reply(text)