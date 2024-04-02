from tgblogparser.config import client
from .config import redis_db


class RedisWorker:
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
