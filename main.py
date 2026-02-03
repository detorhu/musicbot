import asyncio
from pyrogram import idle

from bot.client import bot, assistant
from bot.player.call import start_call


async def main():
    try:
        print("🤖 Starting Bot...")
        await bot.start()

        print("🎧 Starting Assistant...")
        await assistant.start()

        print("📞 Initializing Voice Call...")
        await start_call()

        print("🎶 Music Bot Started Successfully")
        await idle()

    except Exception as e:
        print("❌ ERROR while starting bot:", e)

    finally:
        print("🛑 Stopping Bot...")
        await bot.stop()
        await assistant.stop()


if __name__ == "__main__":
    asyncio.run(main())
