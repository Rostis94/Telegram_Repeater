from telethon import TelegramClient, events
from datetime import datetime
import Secrets
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

client = TelegramClient('user', Secrets.telegram_api_id, Secrets.telegram_api_hash)


@client.on(events.NewMessage(chats=Secrets.source_channel_id))
async def handle_message(event):
    # await event.message.forward_to(Secrets.destination_channel_id)
    await client.send_message(Secrets.destination_channel_id, event.message)
    print(f'{datetime.now():%H:%M:%S} {event.raw_text}')


client.start()
client.run_until_disconnected()
