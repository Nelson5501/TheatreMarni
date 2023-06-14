from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.conf import settings
from unittest import loader
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def home(request):
    return render(request, "home.html")

def photos(request):
    return render(request, "photos.html")

def presentation(request):
    return render(request, "presentation.html")

def catalogue(request):
    return render(request, "catalogue.html")

def dashboard(request):
    return render(request, "dashboard.html")    

def navbar(request):
    return render(request, 'navbar.html', {'request': request})

def signup(request):
    return render(request, 'signup.html', {'request': request})


def login(request):
    return render(request, 'login.html', {'request': request})


def password(request):
    return render(request, 'password.html', {'request': request})


def start(request):
    return render(request, 'start.html', {'request': request})

def start(request):
    return render(request, 'start.html/catalogue.html', {'request': request})


def confirmation(request):
    user_confirmed = True
    return redirect('home')