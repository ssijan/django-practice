from django.http import HttpResponse    
from django.shortcuts import render
import string

def index(request):
    return render(request, 'text.html')

def removepunc(request):
    curr_text = request.POST.get('text','default')
    check = request.POST.get('check','off')
    # print(check)
    if check == 'on':
        removed_pn = ''.join(ch for ch in curr_text if ch not in string.punctuation )
    else:
        removed_pn = curr_text

    return render(request, 'analyzer.html', {'removed':removed_pn})