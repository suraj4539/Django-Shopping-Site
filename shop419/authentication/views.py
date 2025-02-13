from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views.generic import CreateView

# importing django.contrib.auth's user creation 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView # type: ignore

# Create your views here.

class UserRagister(CreateView):
    form_class = UserCreationForm # specifing 
    template_name = 'register.html'
    success_url = reverse_lazy('signin')

class Login(LoginView):
    template_name = 'login.html'