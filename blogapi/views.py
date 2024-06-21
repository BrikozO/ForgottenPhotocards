from rest_framework import generics
from drf_spectacular.utils import extend_schema

from blogsite.models import Post, Picture
from .serializers import PostSerializer, PictureSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'grouped_id'


class AllPicturesList(generics.ListCreateAPIView):
    serializer_class = PictureSerializer

    def get_queryset(self):
        return Picture.objects.all().prefetch_related('categories').select_related('picture_post')


class PicturesOfPostList(generics.ListCreateAPIView):
    serializer_class = PictureSerializer

    def get_queryset(self):
        post_id = self.kwargs['grouped_id']
        return Picture.objects.filter(picture_post=post_id).prefetch_related('categories').select_related('picture_post')

    @extend_schema(operation_id='api_v1_pictures_of_post_list')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(operation_id='api_v1_pictures_of_post_create')
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PictureView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PictureSerializer
    lookup_url_kwarg = 'filename'
    lookup_field = 'image_filename'

    def get_queryset(self):
        post_id = self.kwargs['grouped_id']
        return Picture.objects.filter(picture_post=post_id).prefetch_related('categories').select_related('picture_post')