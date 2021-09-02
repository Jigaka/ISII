from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth import logout
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from apps.user.models import User
from apps.user.forms import UserForm
# Create your views here.

class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'inicio.html'


def logout_Usuario(request):
    logout(request)
    return HttpResponseRedirect('/')


class ListarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = User
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'user/listar_usuario.html'
    queryset = User.objects.all()


class ActivosUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = User
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'user/listar_userActivos.html'
    queryset = User.objects.filter(is_active=True)


class ActualizaUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = User
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'user/actualizar_usuario.html'
    form_class = UserForm
    success_url = reverse_lazy('usuarios:listar_usuario')

class EliminarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = User
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    def post(self,request,pk,*args,**kwargs):#Eliminacion logica
        object = User.objects.get(id = pk)
        object.is_active = False
        object.save()
        return redirect('usuarios:listar_usuario')
