import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e3ae4f861b9b927a14a78.mp4",
        caption=f"""**ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴍᴏɴɢᴏᴅʙ ᴡɪᴛʜ ᴀɪ ꜰᴇᴀᴛᴜʀᴇꜱ ...
💞 ᴛʜᴀɴᴋꜱ ꜰᴏʀ  
ᴜꜱɪɴɢ [ʀᴏᴄᴋs ᴍᴜsɪᴄ](t.me/{BOT_USERNAME}).\nᴍʏ [ᴅᴇᴠᴇʟᴏᴘᴇʀ](t.me/Dr_Asad_Ali) ᴍʏ [sᴜᴘᴘᴏʀᴛᴇʀ](t.me/HarshitSharma361)\n
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⚙️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("👩‍💻 ʙᴀsɪᴄ ɢᴜɪᴅᴇ 👩‍💻 ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅs︎ 📚", callback_data="cbcmds"),
                    InlineKeyboardButton("💝 ᴏᴡɴᴇʀ 💝", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 ɢʀᴏᴜᴘ 👥︎", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 ᴄʜᴀɴɴᴇʟ 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👑 ᴋɪɴɢ 👑", url="https://t.me/Dr_Asad_Ali"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/163e51ab720f0085c53a5.jpg",
        caption=f"""ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💞", url=f"https://t.me/Shayri_Music_Lovers")
                ]
            ]
        ),
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello Sweet Heart ❣️ How Are You** {message.from_user.mention()}</b>

**Yᴏᴜ ᴄᴀɴ ғɪɴᴅ ʜᴇʀᴇ sᴇᴠᴇʀᴀʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜ ʙʀɪᴇғ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ ɢɪᴠᴇ ᴍᴇ [ʜᴇᴀʀᴛ](https://t.me/Give_Me_Heart)👇 !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="🤔 Hᴏᴡ ᴛᴏ ᴜsᴇ Mᴇ 🤔", callback_data="cbguide")]]
        ),
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} Sᴡᴇᴇᴛ Hᴇᴀʀᴛ ❤️ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ !</b>

**Yᴏᴜ ᴄᴀɴ ғɪɴᴅ ʜᴇʀᴇ sᴇᴠᴇʀᴀʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜ ʙʀɪᴇғ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ 👇**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 ʙᴀsɪᴄ ᴄᴍᴅ 📚", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴍᴅ 📕", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 ᴀᴅᴍɪɴ ᴄᴍᴅ 📘", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 sᴜᴅᴏ ᴄᴍᴅ 📗", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 ᴏᴡɴᴇʀ ᴄᴍᴅ 📙", callback_data="cbowner")],
                [InlineKeyboardButton("📔 ғᴜɴ ᴄᴍᴅ 📔", callback_data="cbfun")],
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ᴍs`\n" f"⚡️ Bʏ Asᴀᴅ Aʟɪ` ")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 **Bot Status**:\n"
        f"• **Uᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"• **Sᴛᴀʀᴛ Tɪᴍᴇ:** `{START_TIME_ISO}`"
    )
    
    
@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/336e006861a2667a7663f.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://github.com/jankarikiduniya")
                ]
            ]
        ),
    )

@Client.on_message(command(["owner", "king"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1771e4f5fb861c6f9749e.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴍʏ ᴏᴡɴᴇʀ ɪs [Asᴀᴅ Aʟɪ](t.me/Dr_Asad_Ali")
                ]
            ]
        ),
    )
