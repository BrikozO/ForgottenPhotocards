from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='posts_list'),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path('pictures/', AllPicturesList.as_view(), name='pictures_list'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger_ui'),
    path('<slug:id>/', PostDetail.as_view(), name='post_detail'),
    path('pictures/<slug:grouped_id>/', PicturesOfPostList.as_view(), name='pictures_of_post'),
    path('pictures/<slug:grouped_id>/<slug:filename>/', PictureView.as_view(), name='picture_detail'),
]
