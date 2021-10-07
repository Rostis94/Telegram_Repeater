from telethon import TelegramClient
import Secrets

client = TelegramClient('user', Secrets.telegram_api_id, Secrets.telegram_api_hash)


async def main():
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

# You can print all the dialogs/conversations that you are part of:
with client:
    client.loop.run_until_complete(main())
