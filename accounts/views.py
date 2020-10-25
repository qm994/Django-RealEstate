from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
# Create your views here.

def login(request):
    if request.method == 'POST':
        print('Submit the form!')
        # login the user
        pass
    else:
        return render(request, template_name='accounts/login.html')

def register(request):
    if request.method == 'POST':
        print('Submit the form!')
        # register the user
        pass
    else:
        return render(request, template_name='accounts/register.html')

def dashboard(request):
    
    return render(request, template_name='accounts/dashboard.html')

def logout(request):
    # redirect to the index view, and the view will be retrieved by reverse()
    return redirect('index')
