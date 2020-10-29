from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contacts = Contacts(listing=listing, listing_id=listing_id, name=name,
            email=email, phone=phone, message=message, user_id=user_id)
        contacts.save()

        messages.success(request, 'You request has been submitted! I will get back to u soon!')

    return redirect('/listings/' + listing_id)

