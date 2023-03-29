from django.shortcuts import render, redirect
from .import views
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # fetch all the fields from this request post
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            # make user object
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Successful.')
            return redirect('register')


    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        #  return user object
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            #   messages.success(request, 'You are logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return redirect('login')

    return render(request, 'accounts/login.html')
def logout(request):
    return 
