from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.comments.models import Post
from blog.posts.serializers import PostSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from blog.permissions import IsInPostCreatorGroup


@api_view(["GET"])
def get_posts(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    posts = serializer.data
    # 404 error if no posts
    if len(posts) == 0:
        return Response(status=404, data={"message": "No posts found"})

    return Response(data={"posts": posts, "message": "Posts found"})


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsInPostCreatorGroup])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsInPostCreatorGroup])
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(status=204)


@api_view(["PUT"])
@permission_classes([IsAuthenticated, IsInPostCreatorGroup])
def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_post(request, slug):
    print(slug)
    post = Post.objects.get(slug=slug)
    serializer = PostSerializer(post)
    return Response(serializer.data)
