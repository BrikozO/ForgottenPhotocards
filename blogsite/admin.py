from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.admin.options import TabularInline

from .models import Post, Picture, PictureCategory


class PictureCategoryInline(TabularInline):
    model = Picture.categories.through
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'camera', 'lens', 'film', 'publish_date')


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('picture_post', 'picture_image', 'image_filename', 'picture_categories')
    fields = ['picture_post', 'picture_image', 'image_filename']
    inlines = [PictureCategoryInline]
    readonly_fields = ['picture_image']

    @admin.display(description='Изображение', empty_value="Нет фото")
    def picture_image(self, picture: Picture):
        return mark_safe(f"<img src='{picture.image.url}' width='50'/>")

    @admin.display(description='Категории')
    def picture_categories(self, picture: Picture):
        return [category.category for category in picture.categories.all()]


@admin.register(PictureCategory)
class PictureCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    ordering = ['id']
