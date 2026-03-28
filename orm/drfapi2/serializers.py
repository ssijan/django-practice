from rest_framework import serializers
from .models import TeacherInfo


class TeacherInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherInfo
        fields = '__all__'