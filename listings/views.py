from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Listing
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
#Django uses request and response objects to pass state through the system.

# The `template_name` will access the `templates` folder and this is setup in the coreapp settings.py file
def index(request):
    # only show the published one
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, per_page=6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    print(paged_listings)
    
    context = {
        'listings': paged_listings
    }
    return render(request, template_name='listings/listings.html', context=context)

def listing(request, listing_id):
    return render(request, template_name='listings/listing.html')

def search(request):
    return render(request, template_name='listings/search.html')