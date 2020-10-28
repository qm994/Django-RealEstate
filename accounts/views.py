from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
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
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, template_name='accounts/register.html')

def dashboard(request):
    
    return render(request, template_name='accounts/dashboard.html')

def logout(request):
    # redirect to the index view, and the view will be retrieved by reverse()
    return redirect('index')
