from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
#Django uses request and response objects to pass state through the system.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, template_name='pages/index.html', context=context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    # get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, template_name='pages/about.html', context=context)