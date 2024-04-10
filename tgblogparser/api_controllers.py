import aiohttp
from telethon.tl.types import MessageService
from tgblogparser.config import client, channel
from tgblogparser.objects.basic_objects import clear_pictures_cache
from tgblogparser.tg_handlers import get_telegram_post, get_telegram_picture


async def get_posts(messages):
    async with aiohttp.ClientSession() as session:
        for message in messages:
            if message.text != "":
                post = await get_telegram_post(message)
                if not await post.get_request(session):
                    yield post
            if message.photo is not None:
                picture = await get_telegram_picture(message)
                if not await picture.get_request(session):
                    yield picture


@clear_pictures_cache
async def update_posts():
    messages = await get_client_messages()
    async for elem in get_posts(messages):
        async with aiohttp.ClientSession() as session:
            await elem.post_request(session)


async def get_client_messages():
    async with client:
        return (msg for msg in await client.get_messages(channel, reverse=True, limit=None) if
                not isinstance(msg, MessageService))


__all__ = ['get_posts', 'update_posts']
