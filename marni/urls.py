from django.urls import path, include
from .views import home, photos, presentation

urlpatterns = [
    path('', home, name="marni-homepage"),
    path('photos/', photos, name="marni-pagephoto"),
    path('Presentation/', presentation, name='marni-presentation'),

]