from django.contrib import admin

# Register your models here.
from .models import Listing
# Register your models here.
# this is where we customize the admin for the listing app

admin.site.register(Listing)