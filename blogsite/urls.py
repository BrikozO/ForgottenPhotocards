from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('adminpage/', AdminPageView.as_view(), name='adminpage')
]
