from django.contrib import admin


from .models import Course
from .models import Learnings

admin.site.register(Course)
admin.site.register(Learnings)
