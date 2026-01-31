from pyrogram import filters
from pyrogram.errors import ChatAdminRequired
from musicbot import bot
from config import OWNER_ID
from utils.queue import reset_queue
from utils.vc import vc


def is_admin(_, __, m):
    try:
        member = m.chat.get_member(m.from_user.id)
        return member.status in ("administrator", "creator")
    except ChatAdminRequired:
        return False


@bot.on_message(filters.command("vcend") & filters.group)
async def vc_end(_, m):
    if not is_admin(_, None, m):
        return await m.reply("❌ Sirf admin use kar sakta hai")

    reset_queue(m.chat.id)
    await vc.leave_group_call(m.chat.id)
    await m.reply("🛑 VC band kar diya + queue clear")


@bot.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart(_, m):
    await m.reply("♻️ Bot restart ho raha hai...")
    exit(0)
