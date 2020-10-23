from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
# Create your views here.

def login(request):
    
    return render(request, template_name='accounts/login.html')

def register(request):
    
    return render(request, template_name='accounts/register.html')

def dashboard(request):
    
    return render(request, template_name='accounts/dashboard.html')

def index(request):
    pass

def logout(request):
    # redirect to the index view, and the view will be retrieved by reverse()
    return redirect('index')
