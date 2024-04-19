import os
import types

import aiohttp
from django.core.cache import cache

from redisdb import RedisWorker
from tgblogparser.config import client, http_session
from ._errors import AuthorizationError
from ._objects import BasicURL


class AuthorizationRequired(BasicURL):

    def __init__(self, func):
        self.__func = func
        self.url = super().url + 'auth/token/login/'

    async def __call__(self, *args, **kwargs):
        token: str = await RedisWorker.get_user()
        if token is None:
            token: dict = await self.auth()
            await RedisWorker.set_user(token['auth_token'])
        return await self.__func(*args, **kwargs)

    def __get__(self, instance, owner):
        return types.MethodType(self, instance)

    async def auth(self, login_attempts: int = 5):
        if login_attempts == 0:
            raise AuthorizationError()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        async with http_session as session:
            response = await session.post(self.url, data={"username": username, "password": password})
            if response.status == 200:
                print("U are successfully logged in")
                return await response.json()
            print(f"Invalid username or password! U have only {login_attempts - 1} attempts to log in!")
            return await self.auth(login_attempts - 1)


def download_media(func):
    async def wrapper(message):
        path: str = f"{message.grouped_id}/{message.photo.id}.jpg"
        if not os.path.exists(os.path.abspath(f"../blogdata/post_pictures/{path}")):
            async with client:
                await client.download_media(message, file=f"../blogdata/post_pictures/{path}")
        return await func(message)

    return wrapper


def clear_pictures_cache(func):
    async def wrapper(*args, **kwargs):
        res = await func(*args, **kwargs)
        cache.delete('pictures')
        return res
    return wrapper


__all__ = ['AuthorizationRequired', 'download_media', 'clear_pictures_cache']
