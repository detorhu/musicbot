import logging
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types import StreamType
from bot.client import call

log = logging.getLogger(__name__)

async def play_stream(chat_id: int, stream_url: str):
    try:
        await call.join_group_call(
            chat_id,
            AudioPiped(
                stream_url,
                stream_type=StreamType().pulse_stream
            ),
        )
        log.info(f"▶️ Started streaming in {chat_id}")
        print("🎶 Music started")
    except Exception as e:
        log.error(f"❌ Failed to play stream: {e}")
        raise e


async def stop_stream(chat_id: int):
    try:
        await call.leave_group_call(chat_id)
        log.info(f"⏹ Stopped streaming in {chat_id}")
        print("🛑 Music stopped")
    except Exception as e:
        log.error(f"❌ Failed to stop stream: {e}")
