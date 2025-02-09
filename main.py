import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient, events

load_dotenv()

api_id= os.getenv("api_id")
api_hash= os.getenv("api_hash")
bot_token= os.getenv("bot_token")

client = TelegramClient("task_bot", api_id, api_hash).start(bot_token)

@client.on(events.NewMessage(pattern='(?i).*Hello'))
async def handler(event):
    await event.reply('Hey!')

client.run_until_disconnected()