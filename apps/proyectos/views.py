from typing import List

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProyectoForm, editarUS, editarProyect, CrearUSForm,aprobar_us
from .models import Proyec, RolProyecto, HistoriaUsuario
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy, reverse
from apps.user.models import User, Rol


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
    """Vista basada en clase para mostrar todos los proyectos para el admin"""


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
    form_class = editarProyect
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










#class listarporencargado( ValidarPermisosMixin, ListView):
#    model = Proyec
class AsignarRolProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase, se utiliza para asignar un rol a un proyecto"""
    model = Proyec
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    form_class = ProyectoForm
    template_name = 'proyectos/asignar_rol.html'
    success_url = reverse_lazy('proyectos:listar_proyectos')



def listarProyectoporEncargado(request):
    user = User.objects.get(id=request.user.id)
    proyectos = user.encargado.all()
    return render(request, 'proyectos/listarporencargado.html', {'proyectos': proyectos})



class listarProyectosUsuario(ValidarPermisosMixin, ListView):
    """Vista basada en clase para listar los proyectos en los que se esta
    ya sea como encargado o solo miembro.
    """


    model = Proyec
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        proyectos = user.equipo.all()
        return render(request, 'proyectos/listar_proyectos.html', {'object_list': proyectos})













class CrearUS(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    model = HistoriaUsuario
    form_class = CrearUSForm
    template_name = 'proyectos/crear_US.html'
    success_url = reverse_lazy('proyectos:listar_us')

    def post(self, request, *args, **kwargs):
        """ Funcion para crear un rol con los datos devueltos por el form

        Crea un nuevo rol con los datos devueltos por el form. Tambien relaciona dicho rol
        con el proyecto actual.
        """
        id = request.path.split('/')[-1]
        proyecto = Proyec.objects.get(id=id)
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        prioridad=request.POST['prioridad']
        us=HistoriaUsuario(nombre=nombre, descripcion=descripcion,prioridad=prioridad,proyecto=proyecto)
        us.save()
        return redirect('proyectos:listar_us', id)


class ConfigurarUs(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = HistoriaUsuario
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'proyectos/configurar_us.html'
    form_class = editarUS
    def get_success_url(self):
        return reverse('proyectos:ver_pb', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })

class EditarUs(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = HistoriaUsuario
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'proyectos/configurar_us.html'
    form_class = CrearUSForm
    def get_success_url(self):
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })

class ListarUS(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = HistoriaUsuario
    template_name = 'proyectos/listar_us.html'

    def get(self, request, pk, *args, **kwargs):
        proyecto=Proyec.objects.get(id=pk)
        us=proyecto.proyecto.all()
        return render(request, 'proyectos/listar_us.html', {'object_list': us})


class EliminarUS(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    """ Vista basada en clase, se utiliza para eliminar un proyecto"""
    model = HistoriaUsuario
    def get_success_url(self):
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })

class aprobarUS(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView ):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = HistoriaUsuario
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'proyectos/aprobar_us.html'
    form_class = aprobar_us
    def get_success_url(self):
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })


class ProductBacklog(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = HistoriaUsuario
    template_name = 'proyectos/ver_PB.html'

    def get(self, request, pk, *args, **kwargs):

        proyecto=Proyec.objects.get(id=pk)
        us = proyecto.proyecto.filter(aprobado_PB=True)
        return render(request, 'proyectos/ver_PB.html', {'object_list': us})
