from ._decorators import AuthorizationRequired
from ._objects import BasicURL, BasicSerializer
from redisdb import RedisWorker
from tgblogparser.config import http_session


class ApiPostRequestMixin(BasicURL, BasicSerializer):

    @AuthorizationRequired
    async def post_request(self):
        token: str = await RedisWorker.get_user()
        async with http_session.post(self.url, data=self.serialize(),
                                     headers={"Authorization": f'Token {token}'}) as response:
            if response.status != 201:
                raise Exception(f"Запрос отвалился с кодом {response.status}")


class ApiGetRequestMixin(BasicURL):

    async def get_request(self, *args) -> bool:
        uri: str = self.url
        token: str = await RedisWorker.get_user()
        for arg in args:
            uri += f"{arg}/"

        async with http_session.get(uri, headers={"Authorization": f'Token {token}'}) as response:
            return response.status == 200


__all__ = ["ApiPostRequestMixin", "ApiGetRequestMixin"]
