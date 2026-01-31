import asyncio
import subprocess

processes = {}

async def play_audio(chat_id, file):
    if chat_id in processes:
        processes[chat_id].kill()

    cmd = [
        "ffmpeg",
        "-re",
        "-i", file,
        "-ac", "2",
        "-ar", "48000",
        "-f", "s16le",
        "-"
    ]

    processes[chat_id] = subprocess.Popen(cmd)

def stop_audio(chat_id):
    if chat_id in processes:
        processes[chat_id].kill()
        del processes[chat_id]
