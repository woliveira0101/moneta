from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('moneta'))

    return render(request, 'index.html')

def login(request):
    if request.method != "POST":
        return HttpResponse('Invalid form type.')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        _login(request, user)
        messages.success(request, 'Successfully logged in!')
        return redirect(reverse('index'))
    else:
        messages.error(request, 'Incorrect credentials.')
        return redirect(reverse('index'))

def register(request):
    if request.method != "POST":
        return HttpResponse('Invalid form type.')

    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    user = User.objects.create_user(username, email, password)
    user.save()

    messages.success(request, 'Account successfully created!')
    return render(request, 'index.html')

def logout(request):
    _logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect(reverse('index'))
