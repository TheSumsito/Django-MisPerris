from django.urls import path
from .views import contacto, home, usuario, login, menu, agregar, menuadopt, listaradopt, listaradmin, registraradopt, registraradmin

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('usuario/', usuario, name="usuario"),
    path('login/', login, name="login"),
    path('menuadmin/', menu, name="menuadmin"),
    path('agregar/', agregar, name="agregar"),
    path('menuadopt/', menuadopt, name="menuadopt"),
    path('listaradopt/', listaradopt, name="listaradopt"),
    path('listaradmin/', listaradmin, name="listaradmin"),
    path('registrarse/', registraradopt, name="registraradopt"),
    path('registraradmin/', registraradmin, name="registraradmin")

]
