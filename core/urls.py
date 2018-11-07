from django.urls import path
from .views import contacto, home, login, menu, agregar, menuadopt, listaradopt, listaradmin, registraradopt, registraradmin
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    path('Contactanos/', contacto, name="contacto"),
    path('Registro/', registraradopt, name="usuario"),
    path('Login/', login, name="login"),
    path('Administracion/', menu, name="menuadmin"),
    path('Administracion/Agregar/', agregar, name="agregar"),
    path('Adoptante/', menuadopt, name="menuadopt"),
    path('Adoptante/Listado/', listaradopt, name="listaradopt"),
    path('Administracion/Listado/', listaradmin, name="listaradmin"),
    path('Home/Registrarse/', registraradopt, name="registraradopt"),
    path('Administrador/Registro/', registraradmin, name="registraradmin"),
]
