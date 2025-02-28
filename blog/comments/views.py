from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Post
from .serializers import CommentSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import CommentSerializer
from django.contrib.auth.models import User


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def create_comment(request):
    user_id = request.user.id
    if not user_id:
        return Response(
            {"error": "You need to be logged in to create a comment"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    post_id = request.data.get("post")
    content = request.data.get("content")

    if not content:
        return Response(
            {"error": "Content cannot be empty"}, status=status.HTTP_400_BAD_REQUEST
        )

    # Sprawdzenie, czy ID posta zostało przesłane
    if not post_id:
        return Response(
            {"error": "Post ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    # Pobranie posta z bazy danych
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    # Utworzenie komentarza
    comment = Comment.objects.create(author=user, post=post, content=content)

    # Zwrócenie odpowiedzi z nowo utworzonym komentarzem
    return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
@api_view(["GET"])
def comments(request):
    comments = Comment.objects.all()

    serialized_comments = CommentSerializer(comments, many=True).data
    for comment in serialized_comments:
        comment["author"] = Comment.objects.get(pk=comment["id"]).author.username
    return Response(serialized_comments)
