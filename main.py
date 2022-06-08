import random
from telethon import TelegramClient, events
import asyncio
from config import *


client = TelegramClient('anon', api_id, api_hash)
client.start()


async def message(delay: int):
    while True:
        await asyncio.sleep(delay)
        for ID in ID_LIST:
            try:
                await client.send_message(entity=ID, message='hello world')
            except Exception as ex:
                print(f'This id caused an error:{ID}\n{ex}')


@client.on(events.NewMessage(func=lambda e: e.is_private))
async def answer(event):
    await event.reply(
        ANSWER_LIST[random.randint(0, len(ANSWER_LIST)-1)]
    )


if __name__ == '__main__':
    client.loop.run_until_complete(message(5))
    # client.run_until_disconnected()
