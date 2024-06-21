from tgblogparser.objects.mixins import ApiGetOrPostMixin


class Picture(ApiGetOrPostMixin):
    def __init__(self, grouped_id, path, filename):
        self.url = super().url + "pictures/"
        self.picture_post = grouped_id
        self.image = None
        self.path = path
        self.image_filename = str(filename)

    async def post_request(self):
        with open(f"../blogdata/post_pictures/{self.path}", "rb") as f:
            setattr(self, 'image', f)
            await super().post_request()


class Post(ApiGetOrPostMixin):
    def __init__(self, grouped_id, text, publish_date, camera=None, lens=None, film=None):
        self.grouped_id = grouped_id
        self.text = text
        self.publish_date = publish_date
        self.camera = camera
        self.lens = lens
        self.film = film


__all__ = ['Picture', 'Post']
