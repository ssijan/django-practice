from rest_framework import serializers
from . models import Aiquest

class AiquestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields = ['teacher_name', 'course_name', 'duration', 'seat']

