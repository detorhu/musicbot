from pytgcalls.types.input_stream import AudioPiped
from bot.client import call

async def play_stream(chat_id, url):
    await call.join_group_call(
        chat_id,
        AudioPiped(url)
    )

async def stop_stream(chat_id):
    await call.leave_group_call(chat_id)
