from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail

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

        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquired = Contacts.objects.all().filter(user_id=user_id, listing_id=listing_id)
            # check if the same user has made the same inquiry already
            if has_inquired:
                messages.error(request, 'You have sent the inquiry! Please dont send duplicated ones!')
                return redirect('/listings/'+listing_id)

        contacts = Contacts(listing=listing, listing_id=listing_id, name=name,
                    email=email, phone=phone, message=message, user_id=user_id)
        contacts.save()

        # then send the email to realtor
        #TODO: Debug the send email functionality
        # send_mail(
        #     subject='Property Inquiry',
        #     message=f'Property Inquiry: {listing} from customer {name} with the message: {message}',
        #     from_email='ma791778711@gmail.com',
        #     recipient_list=[realtor_email, '2964497058@qq.com'],
        #     fail_silently=False
        # )
        messages.success(request, 'You request has been submitted! I will get back to u soon!')
        return redirect('/listings/'+listing_id)


