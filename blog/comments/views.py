from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Post
from .serializers import CommentSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_comment(request):
    user = request.user
    post_id = request.data.get("post")
    content = request.data.get("content")

    if not content:
        return Response(
            {"error": "Content cannot be empty"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    comment = Comment.objects.create(user=user, post=post, content=content)
    return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
