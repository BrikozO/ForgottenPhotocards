from redisdb import RedisWorker
from tgblogparser.objects.controllers import update_all_posts, listen_new_messages
from tgblogparser.config import http_session


async def update_posts(token: str = None):
    await RedisWorker.set_token_async(token)
    try:
        await update_all_posts()
    except RuntimeError as e:
        print(f"Сессия программы непредвиденно закрылась: {e}")
    except Exception as e:
        print(f"Программа завершилась с ошибкой: {e}")
    finally:
        await http_session.close()
