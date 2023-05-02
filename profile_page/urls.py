from django.contrib import admin
from django.urls import path, include
from . import views
from profile_page.views import profile_action

app_name="profileapp"
urlpatterns = [
    path('',profile_action, name="profile_"),
]