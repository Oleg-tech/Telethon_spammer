import random
from telethon import TelegramClient, events

from config import *


client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage(func=lambda e: e.is_private))
async def answer(event):
    await event.reply(
        ANSWER_LIST[random.randint(0, len(ANSWER_LIST)-1)]
    )

# Щоб написати всім користувачам: .send Текст повідомлення
@client.on(events.NewMessage(pattern=r"\.send"))
async def message(event):
    if event.chat_id == ADMIN:
        for ID in ID_LIST:
            try:
                await client.send_message(entity=ID, message=event.message.raw_text.replace('.send', ''))
            except Exception as ex:
                print(f'This id caused an error:{ID}\n{ex}')


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
