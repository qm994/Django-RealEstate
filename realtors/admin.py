from django.contrib import admin

from .models import Realtor
# Register your models here.
# this is where we customize the admin for the listing app

admin.site.register(Realtor)
