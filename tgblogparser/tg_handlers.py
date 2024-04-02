from .models import Picture, Post
from tgblogparser.objects.basic_objects import download_media


@download_media
async def get_telegram_picture(message) -> Picture:
    picture = Picture(str(message.grouped_id),
                      f"{message.grouped_id}/{message.photo.id}.jpg",
                      message.photo.id)
    return picture


@download_media
async def get_telegram_post(message) -> Post:
    text: list = message.text.replace("\n\n", "\n").split("\n")
    first_string: str = text.pop(0)
    post: Post = Post(str(message.grouped_id), first_string, message.date.isoformat())
    for string in text:
        match string[:4]:
            case "Ph: ":
                setattr(post, "camera", string)
            case "Lens":
                setattr(post, "lens", string)
            case "Film":
                setattr(post, "film", string)
            case _:
                post.text += string
    return post
