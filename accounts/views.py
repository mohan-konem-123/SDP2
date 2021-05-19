from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as log, logout as lgout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password2 == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already in use..')
                return redirect('register')
            else:
                user = User.objects.create(username=username, email=email, first_name=first_name,
                                            last_name=last_name)
                subject = "Welcome to People Market"
                message = "Hello " + str(
                    first_name + " " + last_name) + ", welcome to our People Market. And thank you for SingingUp in our website. :)"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
                user.set_password(password1)
                user.save()
                print("user {} created!".format(username))
                return redirect('login')
        else:
            messages.info(request, 'passwod not matched..')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            log(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    lgout(request)
    return render(request, 'index.html')