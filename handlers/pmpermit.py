from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import BOT_USERNAME

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"💕Hi there, This is a music assistant service\n**❗️ Rules:**\n👉..No chatting allowed.\n👉..No spam allowed.\n✨𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 @Dr_Asad_Ali🌟")
  return                       