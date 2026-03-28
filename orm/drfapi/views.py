from django.shortcuts import render
from .models import Aiquest
from . serializers import AiquestSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def aiquest_info(request):
    #Complex Data
    info = Aiquest.objects.all()
    
    #Make Native Python Data (Dectionary)
    serializer = AiquestSerializers(info, many = True)

    #Make JSON Data
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')

@csrf_exempt
def aiquest_create(request):
    
    if request.method == 'POST':
        json_data = request.body

        steam = io.BytesIO(json_data)
        python_data = JSONParser().parse(steam)
        serializer = AiquestSerializers(data = python_data)

        if serializer.is_valid():
            serializer.save()
            # msg = {"msg":"Successfully Inserted data"}
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == 'PATCH':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        d = Aiquest.objects.get(id = id)
        serializer = AiquestSerializers(d, data = python_data, partial = True)

        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"Successfully data Updated"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        print(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        info = Aiquest.objects.get(id = id)
        info.delete()

        msg = {"msg":"Successfully data Deleted"}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type = 'application/json')