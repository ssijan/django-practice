from django.db import models

# Create your models here.
class TeacherInfo(models.Model):
    teacher_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    duration = models.IntegerField()
    seat = models.IntegerField()