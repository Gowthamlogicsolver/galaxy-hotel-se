from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from authentication.models import *
from django.contrib.auth.decorators import login_required


def login_action(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=hotelusers.objects.filter(username=username,password=password)
        if user:
            return redirect('{% url "profileapp:profile_" %}')
            # return render(request,'profile.html')
        else:
            return render(request,'error.html')
    else:
        return render(request,'login_.html')

def logout_action(request):
    logout(request)
    return redirect('landing.html') 


