from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts
# Create your views here.


def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user=user)
            messages.success(request, 'You are now log in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
            
    else:
        return render(request, template_name='accounts/login.html')

def register(request):
    if request.method == 'POST':
        
        # get the form values 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # (1) check the passwords if match
        if password != password2:
            messages.error(request, 'The passwords dont match!')    
            return redirect('register')
        else:
            # (2) check if the username is unique
            userExisted = User.objects.filter(username=username).exists()
            emailExisted = User.objects.filter(email=email).exists()
            print(userExisted)
            if userExisted:
                messages.error(request, f"The username:{username} is already existed!")
                return redirect('register')
            else:
                # (3) check the email if existed
                if emailExisted:
                    messages.error(request, f"The email:{email} is already existed!")
                    return redirect('register')
                else:
                    # (4) finally all looks good and create user
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    # (5) login after the register
                    # auth.login(request, user=user)
                    # messages.success(request, 'You are now log in!')
                    # return redirect('index')    
                    # (5) or we can just save the user and dont log in
                    user.save()
                    messages.success(request, 'U are registered and can log in!')
                    return redirect('login')    
    else:
        return render(request, template_name='accounts/register.html')

def dashboard(request):
    user_id = request.user.id
    loggedInUserContacts = Contacts.objects.all().order_by('-contact_date').filter(user_id=user_id)

    context = {
        'contacts': loggedInUserContacts
    }
    return render(request, template_name='accounts/dashboard.html', context=context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!')
        # redirect to the index view, and the view will be retrieved by reverse()
        return redirect('index')
