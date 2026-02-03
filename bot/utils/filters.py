from pyrogram import filters
from pyrogram.types import Message

# 🔹 Check: user admin hai ya nahi
async def is_admin(_, __, message: Message):
    if not message.chat:
        return False

    user = await message.chat.get_member(message.from_user.id)
    return user.status in ("administrator", "creator")


# 🔹 Custom admin filter
admin_filter = filters.create(is_admin)


# 🔹 Check: user VC me hai ya nahi
def user_in_vc(message: Message):
    return message.from_user and message.from_user.is_bot is False


# 🔹 Check: song name diya gaya hai ya nahi
def has_args(message: Message):
    return len(message.command) > 1
