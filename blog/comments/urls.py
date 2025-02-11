from django.urls import path, include
from blog.comments.views import create_comment

urlpatterns = [
    path("create_comment", create_comment),
]
