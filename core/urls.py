from django.urls import path
from .views import registrar, home

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', registrar, name="contacto"),
]
