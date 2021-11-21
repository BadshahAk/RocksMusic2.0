# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit




from pyrogram import filters
from .callsmusic import client
from . import group_call_instances
from .. import queues


@client.on_message(filters.me & filters.command("start"))
async def pl(__, _):
    if _.chat.id in group_call_instances.active_chats:
        queues.put(_.chat.id, 'out.raw')
    else:
        await group_call_instances.set_stream(_.chat.id, 'out.raw')


@client.on_message(filters.me & filters.command("end"))
async def pl(__, _):
    await group_call_instances.stop(_.chat.id)

client.run()


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.
