from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from posts.views import PostsAPIView,PostListAPIView, UpdateDeletePostAPIView

urlpatterns = [
    path('', PostListAPIView.as_view()),
    path('create', PostsAPIView.as_view()),
    path('update/', UpdateDeletePostAPIView.as_view()),
]