from decouple import config


class BasicURL:
    url: str = f"http://{config('BLOGHOST')}:8000/api/v1/"


class BasicSerializer:

    def serialize(self) -> dict:
        return self.__dict__


__all__ = ["BasicURL", "BasicSerializer"]
