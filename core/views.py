from django.shortcuts import render
from .models import Cliente, Region, Ciudad

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
