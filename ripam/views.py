from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method != "POST":
        return HttpResponse('Error')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
