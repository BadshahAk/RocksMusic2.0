# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit



import traceback
import asyncio # Lol! Weird Import!

from asyncio import QueueEmpty

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from callsmusic import callsmusic, queues

from helpers.filters import command
from helpers.decorators import errors, authorized_users_only
from helpers.database import db, dcmdb, Database
from helpers.dbthings import handle_user_status, delcmd_is_on, delcmd_on, delcmd_off
from config import LOG_CHANNEL, BOT_OWNER, BOT_USERNAME
from . import que, admins as fuck


@Client.on_message()
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)

# Back Button
BACK_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Go Back ⬅️", callback_data="cbback")]])

# @Client.on_message(~filters.private)
async def delcmd(_, message: Message):
    if await delcmd_is_on(message.chat.id) and message.text.startswith("/") or message.text.startswith("!"):
        await message.delete()
    await message.continue_propagation()


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        f"""**━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ [ʀᴏᴄᴋs](t.me/Shayri_Music_Lovers) ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.
┏━━━━━━━━━━━━━━━━━┓
┣★ ʙᴏᴛ : [ʀᴇʟᴏᴀᴅᴇᴅ](t.me/{BOT_USERNAME})
┣★ ᴀᴅᴍɪɴ : [ʀᴇғʀᴇsʜᴇᴅ]
┣★ sᴜᴘᴘᴏʀᴛ : [ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs](t.me/AsadSupport)
┗━━━━━━━━━━━━━━━━━┛
🌸 ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴛʜᴇɴ [ʜᴇᴀʀᴛ](t.me/Give_Me_Heart) ᴍᴇ
💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ » ǫᴜᴇsᴛɪᴏɴ
ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/Dr_Asad_Ali)
━━━━━━━━━━━━━━━━━━━**""",
    )


# Control Menu Of Player
@Client.on_message(command(["control", f"controlpanel", "p"]))
@errors
@authorized_users_only
async def controlset(_, message: Message):
    await message.reply_text(
        "**ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴏᴘᴇɴᴇᴅ ᴄᴏɴᴛʀᴏʟ ᴘᴀɴᴇʟ!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴘᴀᴜꜱᴇ ⏸", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "ʀᴇꜱᴜᴍᴇ ▶️", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ꜱᴋɪᴘ ⏩", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "ᴇɴᴅ ⏹", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴍᴜᴛᴇ 🔇", callback_data="cbmute"
                    ),
                    InlineKeyboardButton(
                        "ᴜɴᴍᴜᴛᴇ 🎵", callback_data="cbunmute"
                    )
                ]
            ]
        )
    )



@Client.on_message(command(["pause", f"pause@{BOT_USERNAME}", "p"]))
@errors
@authorized_users_only
async def pause(_, message: Message):
    if callsmusic.pause(message.chat.id):
        await message.reply_photo(
        photo=f"https://telegra.ph/file/5017169a6cc138ecd1000.jpg",
        caption=f"""⏸ **ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴘᴀᴜꜱᴇᴅ ᴛᴏ ʀᴇsᴜᴍᴇ ᴜsᴇ /resume**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"),
                ]
            ]
        ),
    )
    else:
        await message.reply_photo(
        photo=f"https://telegra.ph/file/87e1b57f3713bdff3ca0c.jpg",
        caption=f"""❗️ **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"),
                ]
            ]
        ),
    )

@Client.on_message(command(["resume", f"resume@{BOT_USERNAME}", "r"]))
@errors
@authorized_users_only
async def resume(_, message: Message):
    if callsmusic.resume(message.chat.id):
        await message.reply_photo(
        photo=f"https://telegra.ph/file/fc19d98891c4ba91261c1.jpg",
        caption=f"""🎧 **ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴜᴍᴇᴅ ᴛᴏ ᴘᴀᴜsᴇ ᴜsᴇ /pause**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"),
                ]
            ]
        ),
    )
    else:
        await message.reply_photo(
        photo=f"https://telegra.ph/file/87e1b57f3713bdff3ca0c.jpg",
        caption=f"""❗️ **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"),
                ]
            ]
        ),
    )


@Client.on_message(command(["end", f"end@{BOT_USERNAME}", "stop"]))
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_photo(
        photo=f"https://telegra.ph/file/87e1b57f3713bdff3ca0c.jpg",
        caption=f"""❗️ **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"),
                ]
            ]
        ),
    )
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.stop(message.chat.id)
        await message.reply_photo(
        photo=f"https://telegra.ph/file/20beff13e5a9b9118daf0.jpg",
        caption=f"""✅ **ᴄʟᴇᴀʀᴇᴅ ᴛʜᴇ Qᴜᴇᴜᴇ ᴀɴᴅ ʟᴇꜰᴛ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ!**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"),
                ]
            ]
        ),
    )


@Client.on_message(command(["skip", f"next", "s"]))
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_photo(
        photo=f"https://telegra.ph/file/87e1b57f3713bdff3ca0c.jpg",
        caption=f"""❗️ **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"),
                ]
            ]
        ),
    )
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            await callsmusic.stop(message.chat.id)
        else:
            await callsmusic.set_stream(
                message.chat.id, queues.get(message.chat.id)["file"]
            )

        await message.reply_photo(
        photo=f"https://telegra.ph/file/3234fc59a3c050513de49.jpg",
        caption=f"""⏭ **Sᴋɪᴘᴘᴇᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴏɴɢ**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"),
                ]
            ]
        ),
    )


@Client.on_message(command(["mute", f"mute@{BOT_USERNAME}", "m"]))
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = callsmusic.mute(message.chat.id)

    if result == 0:
        await message.reply_text("🔇 **ᴍᴜᴛᴇᴅ**")
    elif result == 1:
        await message.reply_text("🔇 **ᴀʟʀᴇᴀᴅʏ ᴍᴜᴛᴇᴅ**")
    elif result == 2:
        await message.reply_text("❗️ **ᴠᴄ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ**")


@Client.on_message(command(["unmute", f"unmute@{BOT_USERNAME}", "um"]))
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = callsmusic.unmute(message.chat.id)

    if result == 0:
        await message.reply_text("🔈 **ᴜɴᴍᴜᴛᴇᴅ**")
    elif result == 1:
        await message.reply_text("🔈 **ᴀʟʀᴇᴀᴅʏ ᴜɴᴍᴜᴛᴇᴅ**")
    elif result == 2:
        await message.reply_text("❗️ **ᴠᴄ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ**")


# Music Player Callbacks (Control by buttons feature)

@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if callsmusic.pause(query.message.chat.id):
        await query.edit_message_text("⏸ **sᴏɴɢ ᴘᴀᴜsᴇᴅ**", reply_markup=BACK_BUTTON)
    else:
        await query.edit_message_text("❗️ **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ**", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if callsmusic.resume(query.message.chat.id):
        await query.edit_message_text("🎧 **sᴏɴɢ ʀᴇsᴜᴍᴇᴅ**", reply_markup=BACK_BUTTON)
    else:
        await query.edit_message_text("❗️ **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘᴀᴜꜱᴇᴅ!**", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbend"))
async def cbend(_, query: CallbackQuery):
    if query.message.chat.id not in callsmusic.active_chats:
        await query.edit_message_text("❗️**ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ**", reply_markup=BACK_BUTTON)
    else:
        try:
            queues.clear(query.message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.stop(query.message.chat.id)
        await query.edit_message_text("✅ **ᴄʟᴇᴀʀᴇᴅ ᴛʜᴇ Qᴜᴇᴜᴇ ᴀɴᴅ ʟᴇꜰᴛ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀ**ᴛ!", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbskip"))
async def cbskip(_, query: CallbackQuery):
     if query.message.chat.id not in callsmusic.active_chats:
        await query.edit_message_text("❗️ **ɴᴏᴛʜɪɴɢ ɪꜱ ᴘʟᴀʏɪɴɢ**", reply_markup=BACK_BUTTON)
     else:
        queues.task_done(query.message.chat.id)
        
        if queues.is_empty(query.message.chat.id):
            await callsmusic.stop(query.message.chat.id)
        else:
            await callsmusic.set_stream(
                query.message.chat.id, queues.get(query.message.chat.id)["file"]
            )

        await query.edit_message_text("🗑 Skipped", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    result = callsmusic.mute(query.message.chat.id)

    if result == 0:
        await query.edit_message_text("🔇 **ᴍᴜᴛᴇᴅ**", reply_markup=BACK_BUTTON)
    elif result == 1:
        await query.edit_message_text("🔇 **ᴀʟʀᴇᴀᴅʏ ᴍᴜᴛᴇᴅ**", reply_markup=BACK_BUTTON)
    elif result == 2:
        await query.edit_message_text("❗️ **ᴠᴄ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ**", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    result = callsmusic.unmute(query.message.chat.id)

    if result == 0:
        await query.edit_message_text("🔈 **ᴜɴᴍᴜᴛᴇᴅ**", reply_markup=BACK_BUTTON)
    elif result == 1:
        await query.edit_message_text("🔈  **ᴀʟʀᴇᴀᴅʏ ᴜɴᴍᴜᴛᴇᴅ**", reply_markup=BACK_BUTTON)
    elif result == 2:
        await query.edit_message_text("❗️ **ᴠᴄ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ**", reply_markup=BACK_BUTTON)

@Client.on_message(command(["auth", f"auth@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        return await message.reply("💡 reply to message to authorize user !")
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply(
            "🟢 user authorized.\n\nfrom now on, that's user can use the admin commands."
        )
    else:
        await message.reply("✅ user already authorized!")


@Client.on_message(command(["deauth", f"deauth@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        return await message.reply("💡 reply to message to deauthorize user !")
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply(
            "🔴 user deauthorized.\n\nfrom now that's user can't use the admin commands."
        )
    else:
        await message.reply("✅ user already deauthorized!")

# Anti-Command Feature On/Off

@Client.on_message(filters.command(["delcmd", f"delcmd@{BOT_USERNAME}"]) & ~filters.private)
@authorized_users_only
async def delcmdc(_, message: Message):
    if len(message.command) != 2:
        await message.reply_text("Lol! This isn't the way to use this command 😂! Please read **/help** ☺️")
        return
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "on":
        if await delcmd_is_on(message.chat.id):
            await message.reply_text("Eh! You are already enabled This Service 😉")
            return
        else:
            await delcmd_on(chat_id)
            await message.reply_text(
                "Successfully Enabled Delete Command Feature For This Chat 😇"
            )
    elif status == "off":
        await delcmd_off(chat_id)
        await message.reply_text("Successfully Disabled Delete Command Feature For This Chat 😌")
    else:
        await message.reply_text(
            "Can't Understand What you're talking about! Maybe Read **/help** 🤔"
        )
        
        
        
        
# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.
