import asyncio
from bot.client import bot, assistant
from bot.player.call import start_call

async def main():
    await bot.start()
    await assistant.start()
    await start_call()
    print("🎶 Music Bot Started")
    await idle()

from pyrogram import idle
asyncio.run(main())
