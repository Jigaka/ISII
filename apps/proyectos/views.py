from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProyectoForm
from .models import Proyec

# Create your views here
def crearProyecto(request):
    if request.method == 'POST':
        proyecto_form=ProyectoForm(request.POST)
        if proyecto_form.is_valid():
            proyecto_form.save()
            return redirect("http://127.0.0.1:8000/proyectos/listar_proyectos/")
    else:
        proyecto_form=ProyectoForm()
    return render(request, 'proyectos/crear_proyecto.html', {'proyecto_form':proyecto_form})
def listarProyectos(request):
    proyectos=Proyec.objects.all()
    return render(request, 'proyectos/listar_proyectos.html',{'proyectos':proyectos})
def editarProyecto(request, id):
    proyecto=Proyec.objects.get(id=id)
    if request.method=="GET" :
        proyecto_form=ProyectoForm(instance=proyecto)
    else:
        proyecto_form=ProyectoForm(request.POST, instance=proyecto)
        if proyecto_form.is_valid():
            proyecto_form.save()
        return redirect("http://127.0.0.1:8000/proyectos/listar_proyectos/")
    return render(request, 'proyectos/crear_proyecto.html', {'proyecto_form':proyecto_form})
def eliminarProyecto(request, id):
    proyecto=Proyec.objects.get(id=id)
    if request.method=="POST" :
        proyecto.delete()
        return redirect("proyectos:listar_proyectos")
    return render(request,'proyectos/eliminar_proyecto.html' , {'proyecto':proyecto})