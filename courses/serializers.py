from rest_framework import serializers
from .models import Course, Learnings


class LearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learnings
        fields = ["id", "title"]  # Możesz dodać więcej pól, jeśli potrzebujesz


class CourseSerializer(serializers.ModelSerializer):
    learnings = LearningSerializer(many=True, read_only=True)  # Poprawna definicja

    class Meta:
        model = Course
        fields = [
            "title",
            "slug",
            "description",
            "author",
            "published",
            "price",
            "learnings",  # Powinno być "learnings", a nie "Learnings"
        ]
