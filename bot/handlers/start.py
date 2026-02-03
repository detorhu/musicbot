from pyrogram import filters
from bot.client import bot

@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        "🎶 **Music Bot Alive!**\n\n"
        "Commands:\n"
        "/play <song name or url>\n"
        "/stop\n"
        "/pause\n"
        "/resume",
        disable_web_page_preview=True
    )
