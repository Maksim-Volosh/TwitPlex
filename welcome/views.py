from django.shortcuts import render
from django.template import context
from django.urls import reverse

def index(request):
    current_page = False
    if request.path == '/welcome/':
        current_page = True
        
    context = {
        'current_page': current_page,
    }
        
    return render(request, 'welcome/welcome.html', context=context)