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


    return HttpResponse(template.render(context, request))


def ajout_au_panier(request, produit_id):
    produit = get_object_or_404(produit, id=produit_id)
    #vérifiez si l'utilisateur a deja un panier actif
    panier, created = panier.objects.get_or_create(utilisateur=request.user, produit=produit)

    #si le panier exite déjà, augmentez la quantité de 1
    if not created:
        panier.quantite += 1
        panier.save()


    return redirect('page_panier')# Redirigez l'utilisateur vers la pagh