from rest_framework import generics

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
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PicturesOfPostList(generics.ListCreateAPIView):
    serializer_class = PictureSerializer

    def get_queryset(self):
        post_id = self.kwargs['grouped_id']
        return Picture.objects.filter(picture_post=post_id)


class PictureView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PictureSerializer
    lookup_url_kwarg = 'filename'
    lookup_field = 'image_filename'

    def get_queryset(self):
        post_id = self.kwargs['grouped_id']
        return Picture.objects.filter(picture_post=post_id)