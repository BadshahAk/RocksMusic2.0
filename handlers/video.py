# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit
# 💔༆ _🅡🅾 C⃤🅚🅢_ԹՏԹԺ ༄🇵🇰 【Usᴇʀ_ᴅɪᴇᴅ】

import asyncio
import re

from config import BOT_USERNAME, GROUP_SUPPORT, IMG_1, IMG_2, UPDATES_CHANNEL
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, add_to_queue
from rocksdriver.asad import call_py
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:70]
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["vplay", f"vplay@{BOT_USERNAME}"]) & other_filters)
async def vplay(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url=f"https://t.me/Dr_Asad_Ali"),
                ],
                [
                    InlineKeyboardButton(
                        "👨‍👨‍👧‍👦 Gʀᴏᴜᴘ 👨‍👨‍👧‍👦", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],
            ]
        )

    replied = m.reply_to_message
    chat_id = m.chat.id
    if replied:
        if replied.video or replied.document:
            loser = await replied.reply("📥 **Dᴏᴡɴʟᴏᴀᴅɪɴɢ ᴠɪᴅᴇᴏ...**")
            dl = await replied.download()
            link = replied.link
            if len(m.command) < 2:
                Q = 720
            else:
                pq = m.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await loser.edit(
                        "» __only 720, 480, 360 allowed__ \n💡 **now streaming video in 720p**"
                    )
            try:
                if replied.video:
                    songname = replied.video.file_name[:70]
                elif replied.document:
                    songname = replied.document.file_name[:70]
            except BaseException:
                songname = "Video"
            
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **Sᴏɴɢ ɪs ᴀᴛ ᴡᴀɪᴛɪɴɢ ᴘᴏsɪᴛɪᴏɴ**\n\n🏷 **Name:** [{songname[:15]}]({link})\n🎧 **Request by:** {m.from_user.mention()}\n🔢 **At position »** `{pos}`",
                    reply_markup=keyboard,
                )
            else:
                if Q == 720:
                    amaze = HighQualityVideo()
                elif Q == 480:
                    amaze = MediumQualityVideo()
                elif Q == 360:
                    amaze = LowQualityVideo()
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(dl, HighQualityAudio(), amaze),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"💡 **Sᴏɴɢ ɪs ᴘʟᴀʏɪɴɢ..**\n\n🏷 **Nᴀᴍᴇ:** [{songname[:15]}]({url})\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}",
                    reply_markup=keyboard,
                )
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» Rᴇᴘʟᴀʏ ᴛᴏ ᴀ **Vɪᴅᴇᴏ Fɪʟᴇ** or **Gɪᴠᴇ ᴍᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.**"
                )
            else:
                loser = await m.reply("🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                Q = 720
                amaze = HighQualityVideo()
                if search == 0:
                    await loser.edit("❌ **Nᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ.**")
                else:
                    songname = search[0]
                    url = search[1]
                    asad, ytlink = await ytdl(url)
                    if asad == 0:
                        await loser.edit(f"❌ yt-dl **Issᴜᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ**\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Video", Q
                            )
                            await loser.delete()
                            await m.reply_photo(
                                photo=f"{IMG_1}",
                                caption=f"💡 **Sᴏɴɢ ɪs ᴀᴛ ᴡᴀɪᴛɪɴɢ ᴘᴏsɪᴛɪᴏɴ**\n\n🏷 **Name:** [{songname[:15]}]({url})\n💭 **Cʜᴀᴛ:** `{chat_id}`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}\n🔢 **Pᴏsɪᴛɪᴏɴ »** `{pos}`",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioVideoPiped(ytlink, HighQualityAudio(), amaze),
                                    stream_type=StreamType().pulse_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                                await loser.delete()
                                await m.reply_photo(
                                    photo=f"{IMG_2}",
                                    caption=f"💡 **Sᴏɴɢ ɪs ᴘʟᴀʏɪɴɢ..**\n\n🏷 **Nᴀᴍᴇ:** [{songname[:15]}]({url})\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await m.reply_text(f"🚫 Eʀʀᴏʀ: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                    "» Rᴇᴘʟᴀʏ ᴛᴏ ᴀ **Vɪᴅᴇᴏ Fɪʟᴇ** or **Gɪᴠᴇ ᴍᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.**"
                )
        else:
            loser = await m.reply("🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            amaze = HighQualityVideo()
            if search == 0:
                await loser.edit("❌ **Nᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ.**")
            else:
                songname = search[0]
                url = search[1]
                asad, ytlink = await ytdl(url)
                if asad == 0:
                    await loser.edit(f"❌ yt-dl **Issᴜᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ**\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await loser.delete()
                        await m.reply_photo(
                            photo=f"{IMG_1}",
                            caption=f"💡 **Sᴏɴɢ ɪs ᴀᴛ ᴡᴀɪᴛɪɴɢ ᴘᴏsɪᴛɪᴏɴ**\n\n🏷 **Name:** [{songname[:15]}]({url})\n💭 **Cʜᴀᴛ:** `{chat_id}`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}\n🔢 **Pᴏsɪᴛɪᴏɴ »** `{pos}`",
                                reply_markup=keyboard,
                        )
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(ytlink, HighQualityAudio(), amaze),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await loser.delete()
                            await m.reply_photo(
                                photo=f"{IMG_2}",
                                caption=f"💡 **Sᴏɴɢ ɪs ᴘʟᴀʏɪɴɢ..**\n\n🏷 **Nᴀᴍᴇ:** [{songname[:15]}]({url})\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await m.reply_text(f"🚫 Eʀʀᴏʀ: `{ep}`")


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.

@Client.on_message(command(["vstream", f"vstream@{BOT_USERNAME}"]) & other_filters)
async def vstream(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url=f"https://t.me/Dr_Asad_Ali"),
                ],
                [
                    InlineKeyboardButton(
                        "👨‍👨‍👧‍👦 Gʀᴏᴜᴘ 👨‍👨‍👧‍👦", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],
            ]
        )

    chat_id = m.chat.id
    if len(m.command) < 2:
        await m.reply("» give me a live-link/m3u8 url/youtube link to stream.")
    else:
        if len(m.command) == 2:
            link = m.text.split(None, 1)[1]
            Q = 720
            loser = await m.reply("🔄 **Pʀᴏᴄᴇssɪɴɢ ʟɪᴠᴇ sᴛʀᴇᴀᴍɪɴɢ...**")
        elif len(m.command) == 3:
            op = m.text.split(None, 1)[1]
            link = op.split(None, 1)[0]
            quality = op.split(None, 1)[1]
            if quality == "720" or "480" or "360":
                Q = int(quality)
            else:
                Q = 720
                await m.reply(
                    "» __only 720, 480, 360 Aʟʟᴏᴡᴇᴅ__ \n💡 **Sᴛʀᴇᴀᴍɪɴɢ ɪɴ 720p**"
                )
            loser = await m.reply("🔄 **Pʀᴏᴄᴇssɪɴɢ ʟɪᴠᴇ sᴛʀᴇᴀᴍɪɴɢ...**")
        else:
            await m.reply("**/vstream {link} {720/480/360}**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            asad, livelink = await ytdl(link)
        else:
            livelink = link
            asad = 1

        if asad == 0:
            await loser.edit(f"❌ yt-dl **Issᴜᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ**\n\n» `{ytlink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Live Stream", livelink, link, "Video", Q)
                await loser.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **Sᴏɴɢ ɪs ᴀᴛ ᴡᴀɪᴛɪɴɢ ᴘᴏsɪᴛɪᴏɴ**\n\n🏷 **Name:** [{songname[:15]}]({url})\n💭 **Cʜᴀᴛ:** `{chat_id}`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}\n🔢 **Pᴏsɪᴛɪᴏɴ »** `{pos}`",
                     reply_markup=keyboard,
                )
            else:
                if Q == 720:
                    amaze = HighQualityVideo()
                elif Q == 480:
                    amaze = MediumQualityVideo()
                elif Q == 360:
                    amaze = LowQualityVideo()
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(livelink, HighQualityAudio(), amaze),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, "Live Stream", livelink, link, "Video", Q)
                    await loser.delete()
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"💡 **[Live stream video]({link}) started.**\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await m.reply_text(f"🚫 Eʀʀᴏʀ: `{ep}`")
