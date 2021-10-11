from typing import List
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import CapacidadDiariaEnSprintForm, SprintForm, agregar_hu_form, configurarEquipoSprintform, cambio_estadoHU_form
from .models import CapacidadDiariaEnSprint, Proyec,  Sprint, HistoriaUsuario, User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy, reverse
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginYSuperUser, \
     LoginNOTSuperUser, ValidarPermisosMixinPermisos, ValidarPermisosMixinHistoriaUsuario, ValidarPermisosMixinSprint, ValidarQuePertenceAlProyecto, ValidarQuePertenceAlProyectoSprint

from datetime import date


# Create your views here.
class CrearSprint(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixin, CreateView ):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/crear_sprint.html'
    model = Sprint
    form_class = SprintForm
    success_url = reverse_lazy('proyectos:listar_proyectos')

    def get_form_kwargs(self):
        kwargs = super(CrearSprint,self).get_form_kwargs()
        self.kwargs['id_sprint']=0
        kwargs.update(self.kwargs)
        return kwargs

    def form_valid(self, form):
        proyecto = get_object_or_404(Proyec, id=self.kwargs['pk'])
        form.instance.proyecto = proyecto
        return super(CrearSprint, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        context['proyecto'] = Proyec.objects.get(id=pk)
        return context
    def get_success_url(self):
        return reverse('sprint:listar_sprint', kwargs={'pk': Sprint.objects.get(id=self.object.pk).proyecto.id })


class ListarSprint(LoginYSuperStaffMixin, ValidarQuePertenceAlProyecto, LoginNOTSuperUser, ListView ):
    """ Vista basada en clase, se utiliza para listar las historias de usuarios del sistema del proyecto"""
    model = Sprint
    template_name = 'sprint/listar_sprint.html'
    #permission_required = ('view_proyec', 'change_proyec')



    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyec.objects.get(id=pk)
        sprint=proyecto.proyecto_s.all().order_by('fecha_inicio')
        for s in sprint:
            if (s.estado=='Pendiente'):
                if date.today() >= s.fecha_inicio and date.today() <= s.fecha_fin:
                    Sprint.objects.filter(id=s.id).update(estado='Iniciado')
            if (s.estado=='Iniciado' or s.estado=='Pendiente'):
                if date.today() > s.fecha_fin:
                    Sprint.objects.filter(id=s.id).update(estado='Finalizado')
                    hus = Sprint.objects.get(id=s.id).sprint.all()
                    for hu in hus:
                        if hu.estado != 'QA':
                            HistoriaUsuario.objects.filter(id=hu.id).update(sprint_backlog=False, aprobado_PB=True,
                                                                            prioridad='Alta', estado='Pendiente', estimacion_user=0,estimacion_scrum=0, estimacion=0 )
        #us = proyecto.proyecto.filter(aprobado_PB=False).order_by('-prioridad_numerica','id')
        return render(request, 'sprint/listar_sprint.html', {'proyecto':proyecto, 'object_list': sprint})

class AgregarHU_sprint(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para editar las historias de usuarios del proyecto"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                          'delete_rol', 'change_rol')
    template_name = 'sprint/agregarHU.html'
    form_class = agregar_hu_form

    def get_success_url(self):
        return reverse('proyectos:ver_pb', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id})
    def post(self, request, *args, **kwargs):
        """ Funcion para crear un rol con los datos devueltos por el form

        Crea un nuevo rol con los datos devueltos por el form. Tambien relaciona dicho rol
        con el proyecto actual.
        """
        id = request.path.split('/')[-1]
        HU = HistoriaUsuario.objects.get(id=id)
        sprint = request.POST['sprint']
        HistoriaUsuario.objects.filter(id=id).update(sprint=sprint, sprint_backlog=True, aprobado_PB=False, estado='Pendiente')
        return redirect('proyectos:ver_pb', HU.proyecto_id)


class EliminarSprint(LoginYSuperStaffMixin, ValidarPermisosMixinSprint, LoginNOTSuperUser, DeleteView):
    """ Vista basada en clase, se utiliza para eliminar un proyecto"""
    model = Sprint
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get_success_url(self):
        return reverse('sprint:listar_sprint', kwargs={'pk': Sprint.objects.get(id=self.object.pk).proyecto.id })

class EditarSprint(LoginYSuperStaffMixin, ValidarPermisosMixinSprint, LoginNOTSuperUser, UpdateView):
    """ Vista basada en clase, se utiliza para editar las historias de usuarios del proyecto"""
    model = Sprint
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'sprint/editar_sprint.html'
    form_class = SprintForm

    def get_form_kwargs(self):
        kwargs = super(EditarSprint,self).get_form_kwargs()
        id_sprint=self.kwargs['pk']
        id_proyecto = Sprint.objects.get(id=id_sprint).proyecto.id
        self.kwargs['pk']=id_proyecto
        self.kwargs['id_sprint']=id_sprint
        kwargs.update(self.kwargs)
        return kwargs

    def get_success_url(self):
        return reverse('sprint:listar_sprint', kwargs={'pk': Sprint.objects.get(id=self.object.pk).proyecto.id })

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto= Sprint.objects.get(id=self.object.pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context


class VerSprint(LoginYSuperStaffMixin, ValidarQuePertenceAlProyectoSprint, TemplateView):
    """
        Vista basada en clase para mostrar el menu de un sprint
    """
    permission_required = ('view_proyec', 'change_proyec')

    def get(self, request, *args, **kwargs):
        """
            funcion para renderizar el menu del sprint
        """
        pk=self.kwargs['pk']

        sprint = Sprint.objects.get(id=pk)
        users = Sprint.objects.values_list('equipo', flat=True).filter(id=pk)
        if request.user.pk in users:
            #Estoy dentro del equipo de trabajo#
            estoyEnEquipo=True
        else:
            #Estoy fuera del equipo de trabajo#
            estoyEnEquipo=False

        proyecto=sprint.proyecto

        capacidadCargada=CapacidadDiariaEnSprint.objects.filter(sprint=sprint,usuario=request.user).exists()

        return render(request, 'sprint/sprint.html',{"estoyEnEquipo":estoyEnEquipo,"sprint":sprint,"proyecto":proyecto,"capacidadCargada":capacidadCargada})



class SprintBacklog(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinSprint, ListView):

    model = HistoriaUsuario
    template_name = 'sprint/ver_sb.html'
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get(self, request, pk, *args, **kwargs):
        sprint=Sprint.objects.get(id=pk)
        proyecto=sprint.proyecto
        us = sprint.sprint.filter(sprint_backlog=True,  estado='Pendiente')
        return render(request, 'sprint/ver_sb.html', {'object_list': us,'sprint':sprint,'proyecto':proyecto})

class TablaKanban(LoginYSuperStaffMixin, ListView):
    model = HistoriaUsuario
    template_name = 'sprint/ver_sb.html'
    '''permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')'''
    def get(self, request, pk, *args, **kwargs):
        sprint=Sprint.objects.get(id=pk)

        us = sprint.sprint.all()

        return render(request, 'sprint/kanban.html', {'object_list': us,'sprint':sprint})


class configurarEquipoSprint(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinSprint, UpdateView):
    """ Vista basada en clase, se utiliza para que el developer estime su historia de usuario asignado"""
    model = Sprint
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'sprint/configurar_equipo.html'
    form_class = configurarEquipoSprintform

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto= Sprint.objects.get(id=self.object.pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

    def get_success_url(self):#HistoriaUsuario.objects.get(id=self.object.pk).sprint.id
        return reverse('sprint:ver_sprint', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id })

class Cambio_de_estadoHU(LoginYSuperStaffMixin, LoginNOTSuperUser, UpdateView):
    """ Vista basada en clase, se utiliza para que el developer estime su historia de usuario asignado"""
    model = HistoriaUsuario
    #permission_required = ('view_proyec', 'change_proyec')
    template_name = 'sprint/cambio_estado.html'
    form_class = cambio_estadoHU_form
    def get_success_url(self):#HistoriaUsuario.objects.get(id=self.object.pk).sprint.id
        return reverse('sprint:kanban', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id })

class ListarEquipo(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinSprint, ListView):
    """Vista basada en clase, se utiliza para listar a los miembros del equipo del sprint"""
    model = Sprint
    template_name = 'sprint/listar_equipo.html'
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto= Sprint.objects.get(id=self.object.pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

    def get(self, request, pk, *args, **kwargs):
        sprint = Sprint.objects.get(id=pk)
        equipo = sprint.equipo.all()
        id_proyecto = Sprint.objects.get(id=pk).proyecto.id
        proyecto = Proyec.objects.get(id=id_proyecto)
        print(id_proyecto)
        print("EQUIPO", equipo)
        return render(request, 'sprint/listar_equipo.html', {'sprint':sprint, 'object_list': equipo, 'proyecto': proyecto})

class AsignarCapacidadDiaria(LoginNOTSuperUser,CreateView ):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    #permission_required = ('view_rol', 'add_rol',
    #                       'delete_rol', 'change_rol')
    template_name = 'sprint/asignar_capacidad.html'
    model = CapacidadDiariaEnSprint
    form_class = CapacidadDiariaEnSprintForm
    success_url = reverse_lazy('inicio.html')

    def form_valid(self, form):
        id_sprint=self.kwargs['pk']
        id_user= self.request.user.pk
        usuario = get_object_or_404(User, id=id_user)
        sprint = get_object_or_404(Sprint, id=id_sprint)
        form.instance.usuario = usuario
        form.instance.sprint = sprint
        return super(AsignarCapacidadDiaria, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        sprint = Sprint.objects.get(id=pk)
        context['sprint']=sprint
        context['proyecto'] = sprint.proyecto
        return context
    def get_success_url(self, **kwargs):
        return reverse('sprint:ver_sprint', kwargs={'pk': CapacidadDiariaEnSprint.objects.get(id=self.object.pk).sprint.id })
