from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

def base_viws(request):
    return render(request, "base.html")

class HomePageView(TemplateView) :  
    template_name = 'home.html'



