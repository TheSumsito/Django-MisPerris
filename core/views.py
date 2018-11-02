from django.shortcuts import render
from .models import Contacto, Region,Ciudad, Mascota, Usuario

# Create your views here.
def home(request):
    return render(request, 'Views/Otras/home.htm')    

def contacto(request):
    ciudades=Ciudad.objects.all()
    regiones=Region.objects.all()
    if request.POST:
        correo=request.POST.get("Correo", "")
        run=request.POST.get("Run", "")
        nombre=request.POST.get("Nombre", "")
        fecha=request.POST.get("Fecha", "")
        telefono=request.POST.get("Telefono", "")
        region=request.POST.get("Region", "")
        ciudad=request.POST.get("Ciudad", "")
        tipo=request.POST.get("TipoVivienda", "")

        obj_ciudad=Ciudad.objects.get(IdCiudad=ciudad)
        obj_region=Region.objects.get(IdRegion=region)

        con=Contacto(
            Rut=run,
            Nombre=nombre,
            Correo=correo,
            FechaNaci=fecha,
            Telefono=telefono,
            Vivienda=tipo,
            IdRegion=obj_region,
            IdCiudad=obj_ciudad
        )
        con.save()
        return render(request, 'Views/Otras/contacto.htm',{'ciudad':ciudades, 'region': regiones})
    else:
        return render(request, 'Views/Otras/contacto.htm',{'ciudad':ciudades, 'region': regiones})


def agregar(request):
    if request.POST:
        foto=request.POST.get("Fotografia", "")
        nombre=request.POST.get("Nombre", "")
        desc=request.POST.get("Descripcion", "")
        raza=request.POST.get("Raza", "")
        estado=request.POST.get("Estado", "")

        masc=Mascota(
            Foto=foto,
            Nombre=nombre,
            Descripcion=desc,
            Raza=raza,
            Estado=estado
        )
        masc.save()
        return render(request, 'Views/Administrador/agregar.htm')
    else:
        return render(request, 'Views/Administrador/agregar.htm')

def registraradmin(request):
    if request.POST:
        correo=request.POST.get("Correo", "")
        contrasena=request.POST.get("Pass","")
        tipo="Administrador"
        usu=Usuario(
            Correo=correo,
            Pass=contrasena,
            TipoUsuario=tipo
        )
        usu.save()
        return render(request, 'Views/Administrador/registraradmin.htm')
    else:
        return render(request, 'Views/Administrador/registraradmin.htm')

def registraradopt(request):
    if request.POST:
        correo=request.POST.get("Correo", "")
        password=request.POST.get("Pass", "")
        tipo="Adoptante"
        usu=Usuario(
            Correo=correo,
            Pass=password,
            TipoUsuario=tipo
        )
        usu.save()
        return render(request, 'Views/Otras/registraradopt.htm')
    else:
        return render(request, 'Views/Otras/registraradopt.htm')

def listaradmin(request):
    mascota=Mascota.objects.all()
    return render(request, 'Views/Administrador/listaradmin.htm', {'mascotas':mascota})
def listaradopt(request):
    mascota=Mascota.objects.all()
    return render(request, 'Views/Adoptante/listaradopt.htm', {'mascotas': mascota})




# ! Paginas
def usuario(request):
    return render(request, 'Views/Otras/usuario.htm')
def login(request):
    registrar=request.POST.get("btnRegistrarse")
    if registrar=="Registrarse":
        return render(request, 'Views/Otras/registraradopt.htm')


    return render(request, 'Views/Otras/login.htm')
def menu(request):
    return render(request, 'Views/Administrador/menuadmin.htm')
    
def menuadopt(request):
    return render(request, 'Views/Adoptante/menuadopt.htm')
