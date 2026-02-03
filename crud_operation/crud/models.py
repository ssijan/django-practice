from django.db import models

# Create your models here.
class Info(models.Model):
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    uName = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    zipCode = models.IntegerField()
    image = models.ImageField(upload_to='crud', default='')
    agree = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName