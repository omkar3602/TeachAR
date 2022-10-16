from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Account
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        # print(request.POST)
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Couldn't Login. Please check your credentials.")
    context = {
        'is_login':1,
    }
    return render(request, 'userauth/login.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        data = request.POST
        # print(data)
        name = data['name']
        username = data['username']
        email = data['email']
        password = data['password']
        password2 = data['password2']
        if password == password2:
            if Account.objects.filter(username=username).exists():
                messages.info(request, 'Username not available. Use another username.')
                return redirect('signup')
            elif Account.objects.filter(email=email).exists():
                messages.info(request, 'Email not available. Use another email.')
                return redirect('signup')
            else:
                user=Account.objects.create_user(name=name, username=username, email=email, password=password)
                user.save()
                login(request, user)
                messages.info(request, 'Account created successfully.')
                return redirect('login')
        else:
            messages.error(request, 'Please make sure the passwords match.')
            return redirect('signup')
    context = {
        'is_login':0,
    }
    return render(request, 'userauth/signup.html', context)

def logout_user(request):
    if request.method == 'POST' and request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('home')
    if not request.user.is_authenticated:
        return redirect('home')
    return redirect('home')