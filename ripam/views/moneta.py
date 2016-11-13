from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse

def dashboard(request):
    if not request.user.is_authenticated:
        messages.success(request, 'You must be logged in to access this page.')
        return redirect(reverse('index'))

    return render(request, 'moneta.html')
