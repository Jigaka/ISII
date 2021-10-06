from typing import List
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SprintForm, agregar_hu_form, configurarEquipoSprintform, cambio_estadoHU_form
from .models import Proyec,  Sprint, HistoriaUsuario
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginYSuperUser, LoginNOTSuperUser, ValidarPermisosMixinPermisos, ValidarPermisosMixinHistoriaUsuario
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy, reverse



# Create your views here.
class CrearSprint(LoginNOTSuperUser, ValidarPermisosMixin, CreateView ):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/crear_sprint.html'
    model = Sprint
    form_class = SprintForm
    success_url = reverse_lazy('proyectos:listar_proyectos')

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


class ListarSprint(LoginNOTSuperUser, ListView ):
    """ Vista basada en clase, se utiliza para listar las historias de usuarios del sistema del proyecto"""
    model = Sprint
    template_name = 'sprint/listar_sprint.html'
    #permission_required = ('view_historiausuario', 'delete_historiausuario')



    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyec.objects.get(id=pk)
        sprint=proyecto.proyecto_s.all()
        #us = proyecto.proyecto.filter(aprobado_PB=False).order_by('-prioridad_numerica','id')
        return render(request, 'sprint/listar_sprint.html', {'proyecto':proyecto, 'object_list': sprint})

class AgregarHU_sprint(LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
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
        HistoriaUsuario.objects.filter(id=id).update(sprint=sprint, sprint_backlog=True)
        return redirect('proyectos:ver_pb', HU.proyecto_id)



class VerSprint(TemplateView):
    """
        Vista basada en clase para mostrar el menu de un sprint
    """


    def get(self, request, *args, **kwargs):
        """
            funcion para renderizar el menu del sprint
        """

        # sprint = Sprint.objects.get(id=pk)
        return render(request, 'sprint/sprint.html')



class SprintBacklog(LoginNOTSuperUser, ValidarPermisosMixin, ListView):

    model = HistoriaUsuario
    template_name = 'sprint/ver_sb.html'
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get(self, request, pk, *args, **kwargs):
        sprint=Sprint.objects.get(id=pk)

        us = sprint.sprint.filter(sprint_backlog=True, estado='Pendiente')
        return render(request, 'sprint/ver_sb.html', {'object_list': us,'sprint':sprint})

class TablaKanban( ListView):
    model = HistoriaUsuario
    template_name = 'sprint/ver_sb.html'
    '''permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')'''
    def get(self, request, pk, *args, **kwargs):
        sprint=Sprint.objects.get(id=pk)

        us = sprint.sprint.filter(estado='ToDo')
        return render(request, 'sprint/kanban.html', {'object_list': us,'sprint':sprint})


class configurarEquipoSprint(LoginNOTSuperUser, ValidarPermisosMixin, UpdateView):
    """ Vista basada en clase, se utiliza para que el developer estime su historia de usuario asignado"""
    model = Sprint
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'sprint/configurar_equipo.html'
    form_class = configurarEquipoSprintform
    def get_success_url(self):#HistoriaUsuario.objects.get(id=self.object.pk).sprint.id
        return reverse('sprint:ver_sprint', kwargs={'pk': self.object.pk })

class Cambio_de_estadoHU(LoginNOTSuperUser, UpdateView):
    """ Vista basada en clase, se utiliza para que el developer estime su historia de usuario asignado"""
    model = HistoriaUsuario
    #permission_required = ('view_proyec', 'change_proyec')
    template_name = 'sprint/cambio_estado.html'
    form_class = cambio_estadoHU_form
    def get_success_url(self):#HistoriaUsuario.objects.get(id=self.object.pk).sprint.id
        return reverse('sprint:kanban', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id })
