from typing import List

from django.shortcuts import redirect, render
from .forms import ProyectoForm
from .models import Proyec, RolProyecto
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from apps.user.models import User, Rol

'''

'''




'''
Funcion para crear un proyecto.
En request, se se obtiene todos los parametros del usuario actual
Se devuelve un form para crear un proyecto y guardar en la base de datos.
'''
class CrearProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase, se utiliza para crear permisos"""
    model = Proyec
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    form_class = ProyectoForm
    template_name = 'proyectos/crear_proyecto.html'
    success_url = reverse_lazy('proyectos:listar_proyectos')




class ListarProyectos(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):

    model = Proyec
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'proyectos/listar_proyectos.html'
    queryset = Proyec.objects.all()



'''
Funcion para editar un proyecto.
En request, se se obtiene todos los parametros del usuario actual.
El id representa el id del proyecto a editar
Se devuelve un form para editar un proyecto y actualizar en la base de datos.
'''

class EditarProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = Proyec
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'proyectos/editar_proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyectos:listar_proyectos')


'''
Funcion para eliminar un proyecto.
En request, se se obtiene todos los parametros del usuario actual.
El id representa el id del proyecto a eliminar
Se devuelve un form para confirmar la eliminacion del proyecto.
'''
class EliminarProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    """ Vista basada en clase, se utiliza para eliminar un proyecto"""
    model = Proyec
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    def post(self,request,pk,*args,**kwargs):#Eliminacion logica
        object = Proyec.objects.get(id = pk)
        object.delete()
        return redirect('proyectos:listar_proyectos')


class Proyecto(LoginYSuperStaffMixin, ValidarPermisosMixin,TemplateView):
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    def get(self, request, pk, *args, **kwargs):
        return render(request, 'proyectos/proyecto.html', {'proyecto_id':pk})



class ListadoIntegrantes(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    ''' Vista basada en clase, muestra los integrantes de un proyecto'''

    model = User
    permission_required = ('user.view_user', 'user.add_user',
                               'user.delete_user', 'user.change_user')

    def get(self, request, pk, *args, **kwargs):
        """ Funcion para retornar la lista de integrantes de un proyecto



        Argumentos:
            pk: ID del proyecto

        Returns:
            view: render listado de integrantes
        """


        users = Proyec.objects.get(id=pk).equipo.all()

        ''' Doc para la linea de abajo
            Esta parte es un poco larga.
            Recorre la lista users, para obtener cada user. Luego, de acuerdo al user,obtiene
            su rol dentro del proyecto con el id=pk.
            Para obtener el rol del user, primero trae filtra el rol del user respecto al proyecto,
            ahi se obtiene el id del rol. Con el id del rol, se obtiene el rol del modelo Rol.
        '''
        integrantes = [{'user':user, 'rol': Rol.objects.filter(id = user.rol.filter(proyecto_id=pk).first().rol.id if user.rol.filter(proyecto_id=pk).first() else None ).first()} for user in users]
        proyecto = Proyec.objects.get(id=pk)
        return render(request, 'proyectos/listar_integrantes.html', {'users': integrantes, 'proyecto': proyecto})



class AsignarRolProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase, se utiliza para asignar un rol a un proyecto"""
    model = Proyec
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    form_class = ProyectoForm
    template_name = 'proyectos/asignar_rol.html'
    success_url = reverse_lazy('proyectos:listar_proyectos')