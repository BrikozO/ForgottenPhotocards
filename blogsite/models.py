from datetime import datetime

from django.db import models

from .storage import OverwriteStorage


# Create your models here.
class Post(models.Model):
    grouped_id = models.CharField(max_length=17, verbose_name="Служебный ID", unique=True)
    text = models.TextField(verbose_name="Текст поста")
    camera = models.CharField(max_length=256, blank=True, null=True, verbose_name="Модель камеры")
    lens = models.CharField(max_length=256, blank=True, null=True, verbose_name="Объектив")
    film = models.CharField(max_length=256, blank=True, null=True, verbose_name="Фотопленка")
    publish_date = models.DateTimeField(verbose_name="Дата публикации", default=datetime.now)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['publish_date']

    def __str__(self):
        return self.text


class Picture(models.Model):
    def directory_path(self, filename):
        return f"post_pictures/{self.picture_post.grouped_id}/{filename}"

    picture_post = models.ForeignKey("Post", to_field="grouped_id", on_delete=models.CASCADE, verbose_name="Пост")
    image_filename = models.CharField(verbose_name="Файл изображения", default=None, unique=True, max_length=256)
    image = models.ImageField(upload_to=directory_path, storage=OverwriteStorage(), verbose_name="Изображение")
    categories = models.ManyToManyField('PictureCategory', blank=True, related_name="categories")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ['picture_post', 'image_filename']

    def __str__(self):
        return self.image_filename


class PictureCategory(models.Model):
    class Categories(models.TextChoices):
        ARCHITECTURE = "ARCHITECTURE", "Architecture"
        PORTRAIT = "PORTRAIT", "Portrait"
        URBAN = "URBAN", "Urban"
        EVENT = "EVENT", "Event"
        OTHER = "OTHER", "Other"

    category = models.CharField(max_length=12, choices=Categories.choices, verbose_name="Категория",
                                default=Categories.OTHER, unique=True)

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category
