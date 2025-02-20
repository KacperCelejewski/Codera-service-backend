from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from courses.views import CourseViewSet

router = routers.DefaultRouter()

router.register(r"courses", CourseViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
