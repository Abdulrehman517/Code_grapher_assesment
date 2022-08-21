from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from posts.views import PostsAPIView

urlpatterns = [
    path(r'', PostsAPIView.as_view()),
]