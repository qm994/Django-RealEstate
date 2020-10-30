from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Contacts
# Register your models here.

class ContactsAdmin(ModelAdmin):
    # the model fields we want to display in the admin Contacts Page
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    #list_filter = ('contact_date')
    #list_editable = ('email')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contacts, ContactsAdmin)