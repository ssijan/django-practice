from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    firstName = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to='crud', default='')


    def __str__(self):
        return self.firstName