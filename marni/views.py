from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post


class HomePageView(TemplateView) :  
    template_name = 'home.html'

def page_not_fund_view(request):
    return render(request, 'marni/404.html', context)
    context = {}

