import redis
from decouple import config

redis_db = redis.Redis(host=config("REDIS_HOST"), port=config("REDIS_PORT"), charset="utf-8", decode_responses=True)
redis_db.close()
