from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
#Django uses request and response objects to pass state through the system.
def index(request):
    return render(request, template_name='pages/index.html')

def about(request):
    return render(request, template_name='pages/about.html')