from django.urls import path

# the idea is have the path/url attach to the view so we also need to bring in all the views for pages;
from . import views

urlpatterns = [
    path('', views.index, name = 'listings'),
    # ex: listings/<id>
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search')
]