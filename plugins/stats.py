from pyrogram import filters
from bot import bot
from utils.database import db

stats = db["stats"]


def inc_play(song):
    stats.update_one(
        {"song": song},
        {"$inc": {"count": 1}},
        upsert=True
    )


@bot.on_message(filters.command("stats"))
async def show_stats(_, m):
    top = stats.find().sort("count", -1).limit(10)

    text = "📊 <b>Top Played Songs</b>\n\n"
    i = 1
    for s in top:
        text += f"{i}. {s['song']} — {s['count']} plays\n"
        i += 1

    if i == 1:
        text += "No data yet."

    await m.reply(text)