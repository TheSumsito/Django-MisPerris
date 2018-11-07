from django.shortcuts import render
from .models import Contacto, Region,Ciudad, Mascota, Usuario
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
        nombre=request.POST.get("Nombre", "")
        apellido=request.POST.get("Apellido", "")
        correo=request.POST.get("Correo", "")
        password=request.POST.get("Pass", "")
        repassword=request.POST.get("Repass", "")
        usuario=request.POST.get("User", "")

        usu=User.objects.create_user(
            first_name=nombre,
            last_name=apellido,
            username=usuario, 
            email=correo, 
            password=password
        )

        if password==repassword:
            usu.is_staff=True
            usu.save()
            return render(request, 'Views/Administrador/regadmin.htm')
    else:
        return render(request, 'Views/Administrador/regadmin.htm')

def registraradopt(request):
    if request.POST:
        nombre=request.POST.get("Nombre", "")
        apellido=request.POST.get("Apellido", "")
        correo=request.POST.get("Correo", "")
        password=request.POST.get("Pass", "")
        repassword=request.POST.get("Repass", "")
        username=request.POST.get("User", "")

        usu=User.objects.create_user(
            first_name=nombre,
            last_name=apellido,
            username=username, 
            email=correo, 
            password=repassword
        )
        if password==repassword:
            usu.is_staff=False
            usu.save()
            return render(request, 'Views/Otras/regadopt.htm')
    else:
        return render(request, 'Views/Otras/regadopt.htm')


def listaradmin(request):
    mascota=Mascota.objects.all()
    return render(request, 'Views/Administrador/listar.htm', {'mascotas':mascota})
def listaradopt(request):
    mascota=Mascota.objects.all()
    return render(request, 'Views/Adoptante/listar.htm', {'mascotas': mascota})

def login(request):
    if request.POST:
        correo=request.POST.get("Correo", "")
        password=request.POST.get("Pass", "")
        user=auth.authenticate(username=correo, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            na=request.user.is_staff
            if na==True:
                return render(request, 'Views/Administrador/menu.htm')
            else:
                return render(request, 'Views/Adoptante/menu.htm')
    else:
        return render(request, 'Views/Otras/login.htm')





# ! Paginas
def menu(request):
    return render(request, 'Views/Administrador/menu.htm')
    
def menuadopt(request):
    return render(request, 'Views/Adoptante/menu.htm')


def modificar(request):
    if request.POST:
        accion=request.POST.get("btnAccion","")
        if accion=="Buscar":
            nombre=request.POST.get("NombreBusqueda", "")
            mas=Mascota.objects.get(Nombre=nombre)
            return render(request, 'Views/Administrador/modificar.htm', {'mas':mas})
        if accion=="Actualizar":
            nombremod=request.POST.get("Nombre", "")
            mas=Mascota.objects.get(Nombre=nombremod)

            nombre=request.POST.get("Nombre", "")
            raza=request.POST.get("Raza", "")
            desc=request.POST.get("Descripcion", "")
            estado=request.POST.get("Estado", "")

            mas.Nombre=nombre
            mas.Raza=raza
            mas.Descripcion=desc
            mas.Estado=estado

            mas.save()
            return render(request, 'Views/Administrador/modificar.htm')
    else:
        return render(request, 'Views/Administrador/modificar.htm')

def eliminar(request):
    if request.POST:
        accion=request.POST.get("btnAccion", "")
        if accion=="Buscar":
            nombre=request.POST.get("NombreBusqueda", "")
            mas=Mascota.objects.get(Nombre=nombre)
            return render(request, 'Views/Administrador/eliminar.htm', {'mas':mas})

        if accion=="Eliminar":
            nombre=request.POST.get("Nombre", "")
            mas=Mascota.objects.get(Nombre=nombre)
            mas.delete()
            resp=True
            return render(request, 'Views/Administrador/eliminar.htm', {'mas':mas})
            

    else:
        return render(request, 'Views/Administrador/eliminar.htm')