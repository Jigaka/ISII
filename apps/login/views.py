from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from .models import ListaPermitidos
from .forms import CorreoForm
# Create your views here.

'''
Metodo que muestra al usuario
la pantalla de inicio en que de estar logueado, 
sino muestra la pantalla de inicio de sesion
'''
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('inicio')
    else:
        return HttpResponseRedirect('login')


class AgregarCorreosPermitidos(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """docstring for AgregarCorreosPermitidos."""
    model = ListaPermitidos
    permission_required = ('login.view_listapermitidos', 'login.add_listapermitidos',
                           'login.delete_listapermitidos', 'login.change_listapermitidos')
    form_class = CorreoForm
    template_name = 'login/agregar_correos_permitidos.html'
    success_url = reverse_lazy('login:listar_correos_permitidos')

class ListarCorreosPermitidos(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    """docstring for ListarCorreosPermitidos."""
    model = ListaPermitidos
    permission_required = ('login.view_listapermitidos', 'login.add_listapermitidos',
                           'login.delete_listapermitidos', 'login.change_listapermitidos')
    template_name = 'login/listar_correos_permitidos.html'
    queryset = model.objects.all()

class EliminarCorreosPermitidos(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    """docstring for EliminarCorreosPermitidos."""
    model = ListaPermitidos
    permission_required = ('login.view_listapermitidos', 'login.add_listapermitidos',
                           'login.delete_listapermitidos', 'login.change_listapermitidos')
    def post(self,request,pk,*args,**kwargs):#Eliminacion logica
        object = ListaPermitidos.objects.get(id = pk)
        object.delete()
        return redirect('login:listar_correos_permitidos')
