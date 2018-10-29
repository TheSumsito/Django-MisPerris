from django.db import models

# Create your models here.
class Login(models.Model):
    Usuario=models.EmailField(primary_key=True, max_length=45)
    Pass=models.CharField(max_length=45)

    def __str__(self):
        return self.Usuario

class Region(models.Model):
    IdRegion=models.IntegerField(primary_key=True)
    Descripcion=models.CharField(max_length=45)

    def __str__(self):
        return self.Descripcion
class Ciudad(models.Model):
    IdCiudad=models.IntegerField(primary_key=True)
    Descripcion=models.CharField(max_length=45)
    Region=models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.Descripcion

class Cliente(models.Model):
    Rut=models.CharField(primary_key=True, max_length=45)
    Nombre=models.CharField(max_length=45)
    Correo=models.CharField(max_length=45)
    FechaNaci=models.DateField()
    Telefono=models.IntegerField()
    Vivienda=models.CharField(max_length=45)
    Region=models.ForeignKey(Region, on_delete=models.CASCADE)
    Ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.Rut

class Registro(models.Model):
    Foto=models.FileField()
    Nombre=models.CharField(max_length=45)
    Descripcion=models.TextField(max_length=45)
    Raza=models.CharField(max_length=45)
    Estado=models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre

class Usuario(models.Model):
    Usuario=models.CharField(primary_key=True, max_length=45)
    Pass=models.CharField(max_length=45)
    TipoUsuario=models.CharField(max_length=45)

    def __str__(self):
        return self.Usuario