from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Listing
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from listings.choices import bedroom_choices, price_choices, state_choices
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
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, template_name='listings/listing.html', context=context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    
    print(queryset_list)
    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'values': request.GET
    }
    return render(request, template_name='listings/search.html', context=context)