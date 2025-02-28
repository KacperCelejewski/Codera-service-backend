from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import abc


class SlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) or None

        super().save(*args, **kwargs)


class Category(SlugModel):

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["title"]


class Tag(SlugModel):

    class Meta:
        ordering = ["title"]


class PostManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(published=True)


class Post(SlugModel):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    published = models.BooleanField(default=False)
    objects = PostManager()
    comments = models.ManyToOneRel(to="Comment", field_name="posts", field="id")
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]
