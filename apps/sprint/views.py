from typing import List
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SprintForm, agregar_hu_form
from .models import Proyec,  Sprint
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginYSuperUser, LoginNOTSuperUser, ValidarPermisosMixinPermisos, ValidarPermisosMixinHistoriaUsuario
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy, reverse



# Create your views here.
class CrearSprint( CreateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    #permission_required = ('view_rol', 'add_rol',
     #                      'delete_rol', 'change_rol')
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


class ListarSprint( ListView):
    """ Vista basada en clase, se utiliza para listar las historias de usuarios del sistema del proyecto"""
    model = Sprint
    template_name = 'sprint/listar_sprint.html'
    #permission_required = ('view_historiausuario', 'delete_historiausuario')

    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyec.objects.get(id=pk)
        sprint=proyecto.proyecto_s.all()
        #us = proyecto.proyecto.filter(aprobado_PB=False).order_by('-prioridad_numerica','id')
        return render(request, 'sprint/listar_sprint.html', {'proyecto':proyecto, 'object_list': sprint})

class AgregarHU_sprint(UpdateView):
    """ Vista basada en clase, se utiliza para editar las historias de usuarios del proyecto"""
    model = Sprint
    #permission_required = ('view_rol', 'add_rol',
    #                      'delete_rol', 'change_rol')
    template_name = 'sprint/agregarHU.html'
    form_class = agregar_hu_form
    def get_success_url(self):
        return reverse('sprint:listar_sprint', kwargs={'pk': Sprint.objects.get(id=self.object.pk).proyecto.id})