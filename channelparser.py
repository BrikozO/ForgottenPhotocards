import asyncio

from tgblogparser.api_controllers import update_posts
from tgblogparser.config import client, loop
from redisdb import RedisWorker


async def main(token: str = None):
    if token and await RedisWorker.get_user() is None:
        await RedisWorker().set_user(token)
    await update_posts()


def entrypoint(token: str = None):
    asyncio.set_event_loop(loop)
    with client:
        loop.run_until_complete(main(token))


if __name__ == '__main__':
    entrypoint()
