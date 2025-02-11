from django.contrib import admin
from .comments.models import Post
from .comments.models import Comment

admin.site.register(Post)
admin.site.register(Comment)
