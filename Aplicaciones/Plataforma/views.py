from django.shortcuts import render,redirect

# Create your views here.
from .models import Turno
from .models import Usuario
# Create your views here.

def verlogin(request):
    return render(request,"login.html")
def registrarTurno(request):
    codigo=request.POST['codigo']
    dni=request.POST['dni']
    descripcion=request.POST['descripcion']
    precio=request.POST['precio']
    fecha=request.POST['fecha']
    turno=Turno.objects.create(codigo=codigo,dni=dni,descripcion=descripcion,precio=precio,fecha=fecha)
    turnoslistados=Turno.objects.filter(dni=dni)
    return render(request,"gestionTurnos.html",{"turnos":turnoslistados})
def borrarTurno(request,codigo):
    turno=Turno.objects.get(codigo=codigo)
    dni=turno.dni
    turno.delete()
    turnoslistados=Turno.objects.filter(dni=dni)
    return render(request,"gestionTurnos.html",{"turnos":turnoslistados})
def edicionTurno(request,codigo):
    turno=Turno.objects.get(codigo=codigo)
    return render(request,"edicionTurno.html",{'turno':turno})
def editarTurno(request):
    codigo=request.POST['codigo']
    dni=request.POST['dni']
    descripcion=request.POST['descripcion']
    precio=request.POST['precio']
    fecha=request.POST['fecha']
    turno=Turno.objects.get(codigo=codigo)
    turno.dni=dni
    turno.descripcion=descripcion
    turno.precio=precio
    turno.fecha=fecha
    turno.save()
    turnoslistados=Turno.objects.filter(dni=dni)
    return render(request,"gestionTurnos.html",{"turnos":turnoslistados})
def loguearse(request):
    dni=request.POST['dni']
    contra=request.POST['contra']
    try: 
        usuario=Usuario.objects.get(dni=dni,contra=contra)
        try:
            turnoslistados=Turno.objects.filter(dni=dni)
            return render(request,"gestionTurnos.html",{"turnos":turnoslistados})
        except:
            turnoslistados=[]
            return render(request,"gestionTurnos.html",{"turnos":turnoslistados})
    except:
        return redirect('/')

