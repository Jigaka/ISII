from typing import List
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import Permission, Group
from .forms import ProyectoForm, configurarUSform, editarProyect, CrearUSForm,aprobar_usform, estimar_userform, reasinarUSform
from .models import Proyec, RolProyecto
from apps.sprint.models import HistoriaUsuario, Sprint, Historial_HU
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginYSuperUser, LoginNOTSuperUser, ValidarPermisosMixinPermisos, ValidarPermisosMixinHistoriaUsuario, ValidarPermisosMixinSprint
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




class ListarProyectos(LoginYSuperStaffMixin, LoginYSuperUser, ListView):
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
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/editar_proyecto.html'
    form_class = editarProyect
    success_url = reverse_lazy('proyectos:mis_proyectos')


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
    # permission_required = ('user.view_user', 'user.add_user',
    #                        'user.delete_user', 'user.change_user')
    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyec.objects.get(id=pk)
        return render(request, 'proyectos/proyecto.html', {'proyecto':proyecto, 'proyecto_id':pk})



class ListadoIntegrantes(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    ''' Vista basada en clase, muestra los integrantes de un proyecto'''

    model = User
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')

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


class ExpulsarIntegrantes(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase se utiliza para expulsar un integrante del proyecto"""

    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    model = Proyec
    print("ExpulsarIntegrantes")
    fields = '__all__'
    def get(self, request, *args, **kwargs):
        print(kwargs)
        print(self)
        print(request)
        print(args)
        user = User.objects.get(id = kwargs['pk'])
        proyecto = Proyec.objects.get(id=kwargs['pl'])
        print("USER", user, "PROYECTO", proyecto)
        rol = user.rol.filter(proyecto_id=kwargs['pl']).first()
        print(rol)
        if rol == None:
            proyecto.equipo.remove(user)
            return redirect('proyectos:listar_integrantes', kwargs['pl'])
        grupo =  Group.objects.filter(name=rol.nombre).first()
        print("ROL", rol, "GRUPO", grupo)
        proyecto.equipo.remove(user)
        user.groups.remove(grupo)
        user.rol.remove(rol)
        return redirect('proyectos:listar_integrantes', kwargs['pl'])

#class listarporencargado( ValidarPermisosMixin, ListView):
#    model = Proyec Clase No usada???
class AsignarRolProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase, se utiliza para asignar un rol a un proyecto"""
    model = Proyec
    permission_required = ('view_permission', 'add_permission',
                           'delete_permission', 'change_permission')
    form_class = ProyectoForm
    template_name = 'proyectos/asignar_rol.html'
    success_url = reverse_lazy('proyectos:listar_proyectos')



def listarProyectoporEncargado(request):
    user = User.objects.get(id=request.user.id)
    proyectos = user.encargado.all()
    return render(request, 'proyectos/listarporencargado.html', {'proyectos': proyectos})


class listarProyectosUsuario(LoginYSuperStaffMixin, ListView):
    """Vista basada en clase para listar los proyectos en los que se esta
    ya sea como encargado o solo miembro.
    """


    model = Proyec
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        proyectos = user.equipo.all()
        return render(request, 'proyectos/listar_proyectos.html', {'object_list': proyectos,'title':'Mis proyectos'})


class CrearUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixin, CreateView):

    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    permission_required = ('view_historiausuario', 'add_historiausuario',
                            'delete_historiausuario', 'change_historiausuario')
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
        user = User.objects.get(id=request.user.id)
        us=HistoriaUsuario(nombre=nombre, descripcion=descripcion,prioridad=prioridad,proyecto=proyecto, product_owner=user)
        us.save()
        id_hu=HistoriaUsuario.objects.get(nombre=nombre).id
        Historial_HU.objects.create(descripcion='Creacion de la Historia de Usuario: '+nombre+' id #'+ id_hu.__str__()+' con prioridad: '+prioridad, hu=HistoriaUsuario.objects.get(id=id_hu))
        return redirect('proyectos:listar_us', id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        context['proyecto'] = Proyec.objects.get(id=pk)
        return context

class ConfigurarUs(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/configurar_us.html'
    form_class = configurarUSform


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        id_hu = self.object.pk
        id_proyecto = HistoriaUsuario.objects.get(id=id_hu).proyecto.id
        print(id_proyecto)
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

    def get_success_url(self):
        id_hu = self.object.pk
        Historial_HU.objects.create(
            descripcion='Asignacion de la Historia de Usuario a: ' + HistoriaUsuario.objects.get(
                id=id_hu).asignacion.__str__(), hu=HistoriaUsuario.objects.get(id=id_hu))
        Historial_HU.objects.create(
            descripcion=' Estmacion del Scum Master: ' + HistoriaUsuario.objects.get(
                id=id_hu).estimacion_scrum.__str__(), hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('sprint:ver_sb', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id})




class Reasignar_us(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'sprint/reasingar_us.html'
    form_class = reasinarUSform


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        id_hu = self.object.pk
        id_proyecto = HistoriaUsuario.objects.get(id=id_hu).proyecto.id
        print(id_proyecto)
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

    def get_success_url(self):
        id_hu = self.object.pk
        Historial_HU.objects.create(
            descripcion='Reasignacion de la Historia de Usuario a: ' + HistoriaUsuario.objects.get(
                id=id_hu).asignacion.__str__(), hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('sprint:ver_sb', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id})


class EditarUs(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para editar las historias de usuarios del proyecto"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/editar_us.html'
    form_class = CrearUSForm
    def get_success_url(self):
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })
class ListarUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixin, ListView):

    """ Vista basada en clase, se utiliza para listar las historias de usuarios del sistema del proyecto"""
    model = HistoriaUsuario
    template_name = 'proyectos/listar_us.html'
    permission_required = ('view_historiausuario', 'delete_historiausuario')

    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyec.objects.get(id=pk)
        us = proyecto.proyecto.filter(aprobado_PB=False).order_by('-prioridad_numerica','id')
        return render(request, 'proyectos/listar_us.html', {'proyecto':proyecto, 'object_list': us})


class EliminarUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario,DeleteView):
    """ Vista basada en clase, se utiliza para eliminar un proyecto"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get_success_url(self):
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })

class aprobarUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario,UpdateView ):
    """ Vista basada en clase, se utiliza para aprobar las Historia de Usuario"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/aprobar_us.html'
    form_class = aprobar_usform
    def get_success_url(self):
        id_hu = self.object.pk
        Historial_HU.objects.create(
            descripcion='La Historia de Usuario: ' + HistoriaUsuario.objects.get(
                id=id_hu).nombre+' es aprobada por el Scum Master y pasa al Product Backlog ', hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })


class ProductBacklog(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixin, ListView):

    model = HistoriaUsuario
    template_name = 'proyectos/ver_PB.html'
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get(self, request, pk, *args, **kwargs):
        proyecto=Proyec.objects.get(id=pk)
        us = proyecto.proyecto.exclude(aprobado_PB=False)
        return render(request, 'proyectos/ver_PB.html', {'object_list': us,'proyecto':proyecto})


class Listar_us_a_estimar(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinSprint, ListView):
    """Vista basada en clase, se utiliza para listar las historia de usuario asignados al developer"""
    model = HistoriaUsuario
    template_name = 'sprint/us-a-estimar.html'
    permission_required = ('view_proyec', 'change_proyec')

    def get(self, request, pk, *args, **kwargs):
        sprint =Sprint.objects.get(id=pk)
        user = User.objects.get(id=request.user.id)
        us = sprint.sprint.filter(asignacion=user, sprint_backlog=True, estimacion=0)
        id_proyecto = Sprint.objects.get(id=pk).proyecto.id
        proyecto = Proyec.objects.get(id=id_proyecto)
        return render(request, 'sprint/us-a-estimar.html', {'object_list': us, 'proyecto': proyecto})


class estimarUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para que el developer estime su historia de usuario asignado"""
    model = HistoriaUsuario
    permission_required = ('view_proyec', 'change_proyec')
    template_name = 'sprint/estimar_us.html'
    form_class = estimar_userform

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        print(pk)
        print(self.object.pk)
        id_proyecto = HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id
        print(id_proyecto)
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context


    def get_success_url(self):
        id_hu = self.object.pk
        Historial_HU.objects.create(
            descripcion=' Estmacion del usuario ' + HistoriaUsuario.objects.get(
                id=id_hu).asignacion.getNombreUsuario()+' :' +HistoriaUsuario.objects.get(
                id=id_hu).estimacion_scrum.__str__(), hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('sprint:listar_us_a_estimar', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id })
