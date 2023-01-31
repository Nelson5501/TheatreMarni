from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.template import loader

def home(request):
    return render(request, "home.html")

def photos(request):
    return render(request, "photos.html")

def presentation(request):
    return render(request, "presentation.html")





#def EnJournée(request):
    #return render(request, "home.html")

#def Concerts(request):
    #return render(request, "photos.html")

#def DanceCirque(request):
    #return render(request, "presentation.html")

#def Theatre(request):
    #return render(request, "home.html")

#def Enfants(request):
    #return render(request, "photos.html")

#def Expo(request):
    #return render(request, "presentation.html")

#def Events(request):
    #return render(request, "home.html")

#def IntraMuro(request):
    #return render(request, "photos.html")

#def Touts(request):
    #return render(request, "photos.html")




