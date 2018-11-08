from django.contrib import admin
from .models import Region, Ciudad, Contacto, Mascota, Usuario, ContactoAdopt

# Register your models here.
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Contacto)
admin.site.register(Mascota)
admin.site.register(Usuario)
admin.site.register(ContactoAdopt)