from typing import List
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SprintForm
from .models import Proyec,  Sprint
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginYSuperUser, LoginNOTSuperUser, ValidarPermisosMixinPermisos, ValidarPermisosMixinHistoriaUsuario
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy, reverse



# Create your views here.
class CrearSprint(LoginNOTSuperUser, ValidarPermisosMixin, CreateView):
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