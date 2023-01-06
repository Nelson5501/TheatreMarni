from django.contrib import admin
from django.urls import path, include

handler404 = views.handler404

handler404 = 'marni.views.page_not_found_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marni.urls')),
]


