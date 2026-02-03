import logging
from bot.client import call

log = logging.getLogger(__name__)

async def start_call():
    try:
        await call.start()
        log.info("✅ PyTgCalls started successfully")
        print("🎧 Voice call system ready")
    except Exception as e:
        log.error(f"❌ PyTgCalls failed to start: {e}")
        raise e
