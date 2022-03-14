# plugins by Fariz <@farizjs>
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, BOT_USERNAME
from userbot.utils import toni_cmd


@toni_cmd(pattern="inlineon")
async def _(event):
    await event.edit(f"`Sedang menyalakan inline untuk `@{BOT_USERNAME}` tunggu sebentar...`")
    async with bot.conversation("@BotFather") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=93372553)
            )
            await conv.send_message("/setinline")
            await conv.get_response()
            await conv.send_message(f"@{BOT_USERNAME}")
            await conv.get_response()
            await conv.send_message("Search")
            await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.edit("Harap unblock `@BotFather` dan coba lagi")
        await event.edit(f"**Berhasil Menyalakan Mode Inline untuk `@{BOT_USERNAME}`!**")
