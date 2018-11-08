from django.db import models

# Create your models here.
class Region(models.Model):
    IdRegion=models.IntegerField(primary_key=True)
    Descripcion=models.CharField(max_length=45)

    def __str__(self):
        return self.Descripcion
class Ciudad(models.Model):
    IdCiudad=models.IntegerField(primary_key=True)
    Descripcion=models.CharField(max_length=45)
    IdRegion=models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.Descripcion

        
class Usuario(models.Model):
    Correo=models.CharField(primary_key=True, max_length=45)
    Pass=models.CharField(max_length=45)
    TipoUsuario=models.CharField(max_length=45)

    def __str__(self):
        return self.Correo

class Mascota(models.Model):
    Foto=models.ImageField()
    Nombre=models.CharField(primary_key=True, max_length=45)
    Descripcion=models.TextField(max_length=45)
    Raza=models.CharField(max_length=45)
    Estado=models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre

class Contacto(models.Model):
    Rut=models.CharField(primary_key=True, max_length=45)
    Nombre=models.CharField(max_length=45)
    Correo=models.EmailField(max_length=45)
    FechaNaci=models.DateField()
    Telefono=models.IntegerField()
    Vivienda=models.CharField(max_length=45)
    IdRegion=models.ForeignKey(Region, on_delete=models.CASCADE)
    IdCiudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.Rut 

class ContactoAdopt(models.Model):
    Nombre=models.CharField(max_length=45)
    Telefono=models.IntegerField()
    Mensaje=models.TextField(max_length=250)

    def __str__(self):
        return self.Nombre