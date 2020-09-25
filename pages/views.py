from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from listings.models import Listing

# Create your views here.
#Django uses request and response objects to pass state through the system.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, template_name='pages/index.html', context=context)

def about(request):
    return render(request, template_name='pages/about.html')