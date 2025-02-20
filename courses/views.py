from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


@api_view(["GET"])
def get_courses(request):
    serializer = CourseSerializer(Course.objects.all(), many=True)
    courses = serializer.data
    return Response(courses)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


#
