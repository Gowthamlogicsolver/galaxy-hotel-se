from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from authentication.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required (login_url="login_.html")
def profile_action(request):
    #user = request.user
    #user_data = hotelusers.objects.filter(username=user)
    #context = {'user_data': user_data}
    context={}
    context['dataset'] = hotelusers.objects.all()
    return render(request, 'profile.html', context)
    # context["dataset"] = hotelusers.objects.all()
