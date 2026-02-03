from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import os

# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        
        fname = data.get('fname')
        lname = data.get('lname')
        uname = data.get('uname')
        city = data.get('city')
        state = data.get('state')
        zip = data.get('zip')
        img = request.FILES.get('img')
        ag = data.get('agree') == 'on'
        
        Info.objects.create(
            firstName = fname,
            lastName = lname,
            uName = uname,
            city = city,
            state = state,
            zipCode = zip,
            image = img,
            agree = ag
        )

        return redirect('/crud/')
    
    queryset = Info.objects.all()
   
    
    return render(request,'index.html', {'infos': queryset})

def delete_info(request, id):
    
    obj = get_object_or_404(Info, id=id)

    if obj.image and os.path.isfile(obj.image.path):
        os.remove(obj.image.path)
    
    obj.delete()
    return redirect('/crud/')


def update_info(request, id):
    obj = get_object_or_404(Info, id = id)

    if request.method == "POST":
        data = request.POST
        obj.firstName = data.get('fname')

        if request.FILES.get('img'):
            if obj.image and os.path.isfile(obj.image.path):
                os.remove(obj.image.path)
                obj.image = request.FILES.get('img')
        
        obj.save()  
        return redirect('/crud/')

    return render(request, 'update.html',{'info':obj})
