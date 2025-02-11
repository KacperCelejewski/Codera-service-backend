from django.test import TestCase
from .models import Category, Tag, Post
from django.contrib.auth.models import User
from django.utils import timezone


class TestCategory(TestCase):
    def test_str(self):
        category = Category(title="Test Category")
        category.save()
        self.assertEqual(str(category), "Test Category")

    def test_slug(self):
        category = Category(title="Test Category")
        category.save()
        self.assertEqual(
            category.slug, "test-category"
        )  # Sprawdzamy, czy slug został wygenerowany

    def test_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, "categories")

    def test_ordering(self):
        self.assertEqual(Category._meta.ordering, ["title"])


class TestTag(TestCase):
    def test_str(self):
        tag = Tag(title="Test Tag")
        tag.save()
        self.assertEqual(str(tag), "Test Tag")

    def test_slug(self):
        tag = Tag(title="Test Tag")
        tag.save()
        self.assertEqual(
            tag.slug, "test-tag"
        )  # Sprawdzamy, czy slug został wygenerowany

    def test_ordering(self):
        self.assertEqual(Tag._meta.ordering, ["title"])


class TestPost(TestCase):
    def test_published_manager(self):
        # Tworzymy użytkownika
        user = User.objects.create_user(username="testuser", password="testpassword")

        # Tworzymy posty z unikalnymi tytułami
        post_1 = Post.objects.create(
            title="Test Title 1", content="Test Content 1", author=user, published=True
        )
        post_2 = Post.objects.create(
            title="Test Title 2", content="Test Content 2", author=user, published=False
        )

        # Testujemy, czy możemy uzyskać tylko opublikowane posty
        published_posts = Post.objects.published()
        self.assertIn(post_1, published_posts)
        self.assertNotIn(post_2, published_posts)

    def test_ordering(self):
        self.assertEqual(Post._meta.ordering, ["-created_at"])

    def test_str(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        post = Post.objects.create(title="Test title", author=user)
        self.assertEqual(str(post), "Test title")

    def test_created_at(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        post = Post.objects.create(
            title="Test title",
            content="Test Content",
            author=user,
        )
        self.assertTrue(post.created_at <= timezone.now())

    def test_updated_at(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        post = Post.objects.create(
            title="Test title", content="Test Content", author=user
        )
        self.assertTrue(post.updated_at <= timezone.now())

    def test_author(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        post = Post.objects.create(
            title="Test title", content="Test Content", author=user
        )
        self.assertEqual(post.author, user)

    def test_category(self):
        category = Category.objects.create(title="Test Category")
        user = User.objects.create_user(username="testuser", password="testpassword")
        post = Post.objects.create(
            title="Test title", content="Test Content", author=user, category=category
        )
        self.assertEqual(post.category, category)

    def test_tags(self):
        tag = Tag.objects.create(title="Test Tag")
        user = User.objects.create_user(username="testuser", password="testpassword")
        post = Post.objects.create(
            title="Test title", content="Test Content", author=user
        )
        post.tags.add(tag)
        self.assertIn(tag, post.tags.all())

    def test_published(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        post = Post.objects.create(
            title="Test title", content="Test Content", author=user, published=True
        )
        self.assertTrue(post.published)
