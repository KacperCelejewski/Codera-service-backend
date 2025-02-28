from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer, LearningSerializer

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


@permission_classes([AllowAny])
@api_view(["GET"])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@permission_classes([AllowAny])
@api_view(["GET"])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    courseSerializer = CourseSerializer(course)
    print(courseSerializer.data)
    return Response({"course": courseSerializer.data, "status": 200})
