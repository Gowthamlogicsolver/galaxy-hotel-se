from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *

def signaction(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        ob1=hotelusers()
        ob1.username=username
        ob1.email=email
        ob1.password=password
        ob1.save()
        return render(request,"login_.html")
    else:
        return render(request, 'signup.html')
