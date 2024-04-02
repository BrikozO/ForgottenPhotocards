from aiohttp import ClientSession

from ._decorators import AuthorizationRequired
from ._objects import BasicURL, BasicSerializer
from redisdb import RedisWorker


class ApiPostRequestMixin(BasicURL, BasicSerializer):

    @AuthorizationRequired
    async def post_request(self, session: ClientSession):
        token: str = await RedisWorker.get_user()
        await session.post(self.url, data=self.serialize(), headers={"Authorization": f'Token {token}'})


class ApiGetRequestMixin(BasicURL):

    async def get_request(self, session: ClientSession, *args) -> bool:
        uri: str = self.url
        for arg in args:
            uri += f"{arg}/"
        async with session.get(uri) as response:
            return response.status == 200


__all__ = ["ApiPostRequestMixin", "ApiGetRequestMixin"]
