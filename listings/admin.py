from django.contrib import admin

# Register your models here.
from .models import Listing
# Register your models here.
# this is where we customize the admin for the listing app

class ListingAdmin(admin.ModelAdmin):
    # the model fields we want to display in the admin Listings Page
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)