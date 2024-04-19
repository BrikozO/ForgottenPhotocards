from telethon.tl.types import MessageService
from telethon import events

from tgblogparser.config import client, channel
from tgblogparser.models import Picture, Post
from tgblogparser.objects.basic_objects import clear_pictures_cache
from tgblogparser.objects.tg_handlers import get_telegram_post, get_telegram_picture


async def get_posts(messages):
    for message in messages:
        obj = await get_post_or_picture(message)
        if obj:
            yield obj


async def get_post_or_picture(message):
    if message.text != "":
        post = await get_telegram_post(message)
        if not await post.get_request(post.grouped_id):
            return post
    if message.photo is not None:
        picture = await get_telegram_picture(message)
        if not await picture.get_request(picture.picture_post, picture.image_filename):
            return picture


@clear_pictures_cache
async def update_all_posts():
    messages = await get_all_channel_messages()
    async for elem in get_posts(messages):
        await update_post_or_picture(elem)


async def update_post_or_picture(elem: Post | Picture):
    await elem.post_request()


@client.on(events.NewMessage(chats=channel))
async def listen_new_messages(event):
    print(event.message)


async def get_all_channel_messages():
    async with client:
        return (msg for msg in await client.get_messages(channel, reverse=True, limit=None) if
                not isinstance(msg, MessageService))


__all__ = ['get_posts', 'update_all_posts', 'listen_new_messages']
