import asyncio

from redisdb import RedisWorker
from tgblogparser.config import client, loop
from typing import Callable
from tgblogparser.controller_calls import update_posts


def entrypoint_until_complete(func: Callable = update_posts, token: str = None):
    asyncio.set_event_loop(loop)
    with client:
        loop.run_until_complete(func(token))


def entrypoint_until_disconnected(token: str = None):
    asyncio.set_event_loop(loop)
    with client:
        loop.run_until_complete(set_user_token(token))
        client.run_until_disconnected()


async def set_user_token(token: str):
    await RedisWorker.set_token_async(token)


if __name__ == '__main__':
    entrypoint_until_complete(update_posts)
