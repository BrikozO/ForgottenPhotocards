from decouple import config

from ForgottenPhotocards import settings


class BasicURL:
    if settings.DEBUG:
        url: str = f"http://{config('BLOGHOST')}:8000/api/v1/"
    else:
        f"https://{config('ALLOWED_HOSTS').split(',')[0]}/api/v1/"


class BasicSerializer:

    def serialize(self) -> dict:
        return self.__dict__


__all__ = ["BasicURL", "BasicSerializer"]
