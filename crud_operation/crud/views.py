from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Info
from django.contrib.auth.decorators import login_required
import os
from django.http import HttpResponse

# Create your views here.

def index(request):
    queryset = Info.objects.all()
    
    return render(request,'index.html', {'infos': queryset})

def delete_info(request, id):
    
    obj = get_object_or_404(Info, id=id)

    if obj.image and os.path.isfile(obj.image.path):
        os.remove(obj.image.path)
    
    obj.delete()
    return redirect('/crud/')

@login_required(redirect_field_name='login_page')
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

@login_required(redirect_field_name='login_page')
def add_item(request):
    if request.method == 'POST':
        item = request.POST
        print(item)
        Info.objects.create(
            user = request.user,
            firstName =item.get('name'),
            desc = item.get('desc'),
            image = request.FILES.get('img')
        )

        return redirect('/crud/add_item/')
    

    return render(request, 'add_item.html')

def search_item(request):
    qurey = request.GET.get('search')

    if qurey:
        obj = Info.objects.filter(firstName__icontains = qurey)
        # print(item)
        item = {
            'infos' : obj,
            'val': qurey.capitalize,
            'ln': len(obj)
        }

    return render(request,'index.html', item)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')

        if not User.objects.filter(username = username):
            messages.error(request, 'Invalid Username')
            return redirect('login_page')
        
            user = authenticate(request, username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong Password')
            return redirect('login_page')
        
              

    return  render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        fname = request.POST.get('name') 
        username = request.POST.get('username') 
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.error(request, 'Username already taken!')

            return render(request, 'registration.html')
            

        user = User.objects.create_user(
            first_name = fname,
            username = username,
            password = password
        )
        user.save()
        messages.success(request, "Account Created Successfully...")
        return redirect('/crud/register/')

    return  render(request, 'registration.html')

def logOut(request):
    logout(request)
    return redirect('login_page')