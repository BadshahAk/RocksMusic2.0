# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit

import asyncio

from pyrogram import Client

print("Enter your app information from my.telegram.org/apps below.")


async def main():
    async with Client(
        session_name=":memory:",
        api_id=int(input("API ID: ")),
        api_hash=input("API HASH: "),
    ) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
