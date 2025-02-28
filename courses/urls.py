from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from courses.views import get_course, get_courses


urlpatterns = [
    path("admin/", admin.site.urls),
    path("get_courses", get_courses),
    path("get_course/<slug:slug>", get_course),
]
