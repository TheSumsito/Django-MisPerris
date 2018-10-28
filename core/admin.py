from django.contrib import admin
from .models import Login, Region, Ciudad, Cliente

# Register your models here.
admin.site.register(Login)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Cliente)
