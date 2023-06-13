from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marni.urls')),


    
]   
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
