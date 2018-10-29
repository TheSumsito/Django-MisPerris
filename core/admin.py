from django.contrib import admin
from .models import Login, Region, Ciudad, Cliente, Registro, Usuario

# Register your models here.
admin.site.register(Login)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Registro)
admin.site.register(Usuario)