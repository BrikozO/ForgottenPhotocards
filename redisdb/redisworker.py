from redisdb.config import redis_db
from tgblogparser.config import client


class RedisWorker:

    @classmethod
    async def set_token_async(cls, token):
        if token and await cls.get_user() is None:
            await cls.set_user(token)

    @staticmethod
    async def get_user() -> str:
        async with client:
            client_info = await client.get_me()
            return redis_db.get(client_info.id)

    @staticmethod
    async def set_user(token: str, expire_time: int = 3600) -> None:
        async with client:
            client_info = await client.get_me()
            redis_db.set(client_info.id, token, expire_time)


__all__ = ["RedisWorker"]
