# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit


from os import path

from yt_dlp import YoutubeDL

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError

ytdl = YoutubeDL(
    {
        "format": "bestaudio/best",
        "geo-bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "downloads/%(id)s.%(ext)s",
    }
)


def download(url: str) -> str:
    info = ytdl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"**Sᴏʀʀʏ Bʀᴏ! Vɪᴅᴇᴏs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {DURATION_LIMIT} ᴍɪɴᴜᴛᴇ(s) ᴀʀᴇɴ’ᴛ ᴀʟʟᴏᴡᴇᴅ, ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴠɪᴅᴇᴏ ɪs {duration} ᴍɪɴᴜᴛᴇ(s) . Dᴏɴᴀᴛᴇ ᴛᴏ ɪɴᴄʀᴇᴀsᴇ Tɪᴍᴇ Lɪᴍɪᴛ**"
        )

    ytdl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
