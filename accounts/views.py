from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password1']

        if password2 == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                print('Email is already in use..')
            else:
                user = User(username=username, password=password1, email=email, first_name=first_name,
                                            last_name=last_name)
                user.save()
                print("user {} created!".format(username))
        else:
            print('passwod not matched..')
        return redirect('/')
    else:
        return render(request, 'register.html')
