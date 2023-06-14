from django.urls import path, include
from .views import home, photos, presentation, dashboard, catalogue, login, signup, start, password
from django.conf import settings
#from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#from . import views
#from .views import ajouter_au_panier
from django.urls import path





urlpatterns = [

    path('', home, name="marni-homepage"),
    path('photos/', photos, name="marni-photo"),
    path('Presentation/', presentation, name='marni-presentation'),
    path('dashboard/', dashboard, name='marni-dashboard'),
    path('catalogue/', catalogue, name='marni-catalogue'),
    path('start/catalogue/', catalogue, name='marni-catalogue'),
    path('login/', login, name='marni-login'),
    path('signup/', signup, name='marni-signup'),
    #path('shop/', shop, name='shop'),
    #user
    #path('user/template/login.html/', views.login, name='marni-login'),
    path('password/', password, name='marni-resetpassword'),
    #fin user



]
       




