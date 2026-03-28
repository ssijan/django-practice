from django.contrib import admin
from .models import TeacherInfo

# Register your models here.

@admin.register(TeacherInfo)

class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'teacher_name',
        'course_name',
        'city',
        'duration',
        'seat'
    ]