from django.urls import path, include
from blog.posts.views import get_posts, create_post, delete_post, update_post, get_post

urlpatterns = [
    path("get_posts", get_posts),
    path("create_post", create_post),
    path("delete_post/<int:pk>", delete_post),
    path("update_post/<int:pk>", update_post),
    path("get_post/<slug:slug>", get_post),
]
