from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer


@api_view(["GET"])
def get_posts(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    posts = serializer.data
    return Response(posts)
