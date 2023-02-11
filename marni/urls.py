from django.urls import path, include
from .views import home, photos, presentation, dashboard

urlpatterns = [
    path('', home, name="marni-homepage"),
    path('photos/', photos, name="marni-pagephoto"),
    path('Presentation/', presentation, name='marni-presentation'),
    path('dashboard/', dashboard, name='marni-dashboard')
]