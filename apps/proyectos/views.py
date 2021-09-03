from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProyectoForm
from .models import Proyec

'''
Funcion para crear un proyecto.
En request, se se obtiene todos los parametros del usuario actual
Se devuelve un form para crear un proyecto y guardar en la base de datos.
'''
def crearProyecto(request):
    if request.method == 'POST':
        proyecto_form = ProyectoForm(request.POST)
        if proyecto_form.is_valid():
            proyecto_form.save()
            return redirect("proyectos:listar_proyectos")
    else:
        proyecto_form = ProyectoForm()
    return render(request, 'proyectos/crear_proyecto.html', {'proyecto_form':proyecto_form})


'''
Funcion para listar un proyecto.
En request, se se obtiene todos los parametros del usuario actual
Se devuelve un listado de todos los proyectos en el sistema.
A esta funcion solo accede el usuario administrador
'''
def listarProyectos(request):
    proyectos=Proyec.objects.all()
    return render(request, 'proyectos/listar_proyectos.html',{'proyectos':proyectos})



'''
Funcion para editar un proyecto.
En request, se se obtiene todos los parametros del usuario actual.
El id representa el id del proyecto a editar
Se devuelve un form para editar un proyecto y actualizar en la base de datos.
'''
def editarProyecto(request, id):
    proyecto=Proyec.objects.get(id=id)
    if request.method == "GET" :
        proyecto_form = ProyectoForm(instance=proyecto)
    else:
        proyecto_form = ProyectoForm(request.POST, instance=proyecto)
        if proyecto_form.is_valid():
            proyecto_form.save()
        return redirect("proyectos:listar_proyectos")
    return render(request, 'proyectos/crear_proyecto.html', {'proyecto_form':proyecto_form})


'''
Funcion para eliminar un proyecto.
En request, se se obtiene todos los parametros del usuario actual.
El id representa el id del proyecto a eliminar
Se devuelve un form para confirmar la eliminacion del proyecto.
'''
def eliminarProyecto(request, id):
    proyecto = Proyec.objects.get(id=id)
    if request.method == "POST" :
        proyecto.delete()
        return redirect("proyectos:listar_proyectos")
    return render(request,'proyectos/eliminar_proyecto.html' , {'proyecto':proyecto})