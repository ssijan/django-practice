from django.shortcuts import render
from .models import TeacherInfo
from . serializers import TeacherInfoSerializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
# Create your views here.


class TeacherInfoList(GenericAPIView, ListModelMixin):
    queryset = TeacherInfo.objects.all()
    serializer_class = TeacherInfoSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class TeacherInfoCreate(GenericAPIView, CreateModelMixin):
    queryset = TeacherInfo.objects.all()
    serializer_class = TeacherInfoSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TeacherInfoUpdate(GenericAPIView,)

'''
Using API_View
@api_view(['GET', 'POST'])
def create_teacherInfo(request):
    if request.method == 'GET':
        quest = TeacherInfo.objects.all()
        serializer = TeacherInfoSerializers(quest, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = TeacherInfoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def show_teacherInfo(request, pk):
    try:
        quest = TeacherInfo.objects.get(id = pk)
    except TeacherInfo.DoesNotExist:
        return Response({'error': 'ID Not Found!'})

    if request.method == 'GET':
        quest = TeacherInfo.objects.get(id = pk)
        serializer = TeacherInfoSerializers(quest)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method in ['PUT', 'PATCH']:
        partial_status = request.method == 'PATCH'
        serializer = TeacherInfoSerializers(quest, data = request.data, partial = partial_status)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        quest.delete()
        return Response({'msg':'Content Successfully Deleted!'})

'''
