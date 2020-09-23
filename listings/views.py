from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Listing
from django.core import serializers

# Create your views here.
#Django uses request and response objects to pass state through the system.

# The `template_name` will access the `templates` folder and this is setup in the coreapp settings.py file
def index(request):
    listings = Listing.objects.all()
    print(listings.values())
    context = {
        'listings': listings
    }
    return render(request, template_name='listings/listings.html', context=context)

def listing(request, listing_id):
    return render(request, template_name='listings/listing.html')

def search(request):
    return render(request, template_name='listings/search.html')