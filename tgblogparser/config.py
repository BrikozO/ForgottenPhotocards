import aiohttp
import asyncio

from decouple import config
from telethon import TelegramClient

api_id = config('API_ID')
api_hash = f'{config("API_HASH")}'
channel = f'{config("PHOTOCARDS_CHANNEL")}'
phone = f'{config("PHONE_NUMBER")}'
password = f'{config("PASSWORD")}'
http_session = aiohttp.ClientSession()

try:
    asyncio.get_event_loop_policy().get_event_loop()
except RuntimeError:
    asyncio.get_event_loop_policy().set_event_loop(asyncio.new_event_loop())
finally:
    client = TelegramClient('parsession', api_id, api_hash, system_version="4.16.30-vxCUSTOM")
    loop = client.loop
