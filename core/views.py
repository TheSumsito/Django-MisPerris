from django.shortcuts import render
from .models import Cliente, Region, Ciudad, Registro,Usuario

# Create your views here.
def home(request):
    return render(request, 'Views/home.htm')    

def registrar(request):
    if request.POST:
        correo=request.POST.get("Correo", "")
        run=request.POST.get("Run", "")
        nombre=request.POST.get("Nombre", "")
        fecha=request.POST.get("Fecha", "")
        telefono=request.POST.get("Telefono", "")
        tipo=request.POST.get("TipoVivienda", "")
        region=request.POST.get("Region", "")
        ciudad=request.POST.get("Ciudad", "")

        cli=Cliente(
            Correo=correo,
            Rut=run,
            Nombre=nombre,
            FechaNaci=fecha,
            Telefono=telefono,
            Vivienda=tipo,
            Region=region,
            Ciudad=ciudad
        )
        cli.save()
        return render(request, 'Views/contacto.htm')
    else:
        return render(request, 'Views/contacto.htm')


def agregar(request):
    if request.POST:
        foto=request.POST.get("Fotografia", "")
        nombre=request.POST.get("Nombre", "")
        desc=request.POST.get("Descripcion", "")
        raza=request.POST.get("Raza", "")
        estado=request.POST.get("Estado", "")

        reg=Registro(
            Foto=foto,
            Nombre=nombre,
            Descripcion=desc,
            Raza=raza,
            Estado=estado
        )
        reg.save()
        return render(request, 'Views/agregar.htm')
    else:
        return render(request, 'Views/agregar.htm')

def registraradmin(request):
    if request.POST:
        usuario=request.POST.get("Usuario", "")
        contrasena=request.POST.get("Pass","")
        tipo="Administrador"
        usu=Usuario(
            Usuario=usuario,
            Pass=contrasena,
            TipoUsuario=tipo
        )
        usu.save()
        return render(request, 'Views/registraradmin.htm')
    else:
        return render(request, 'Views/registraradmin.htm')





# ! Paginas
def usuario(request):
    return render(request, 'Views/usuario.htm')
def login(request):
    return render(request, 'Views/login.htm')
def menu(request):
    return render(request, 'Views/menuadmin.htm')
def menuadopt(request):
    return render(request, 'Views/menuadopt.htm')
def listaradopt(request):
    return render(request, 'Views/listaradopt.htm')
def listaradmin(request):
    return render(request, 'Views/listaradmin.htm')
def registrarse(request):
    return render(request, 'Views/registrarse.htm')