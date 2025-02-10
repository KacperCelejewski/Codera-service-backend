from django.urls import path, include
from blog.views import get_posts, create_post

urlpatterns = [
    path("get_posts", get_posts),
    path("create_post", create_post),
]
