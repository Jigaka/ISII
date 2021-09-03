from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from apps.user.models import User, Rol
from apps.user.forms import UserForm, PermsForm, RolForm
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

class ListarPermisos(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    permisos = Permission
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    template_name = 'user/listar_permisos.html'
    queryset = permisos.objects.all()

class CrearPermisos(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """docstring for CrearPermisos."""
    model = Permission
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    form_class = PermsForm
    template_name = 'user/crear_permisos.html'
    success_url = reverse_lazy('usuarios:listar_permisos')


class ListarRoles(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    roles = Rol
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    template_name = 'user/listar_roles.html'
    queryset = roles.objects.all()

class CrearRoles(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """docstring for CrearRol."""
    model = Rol
    permission_required = ('auth.view_rol', 'auth.add_rol',
                           'auth.delete_rol', 'auth.change_rol')
    form_class = RolForm
    template_name = 'user/crear_rol.html'
    success_url = reverse_lazy('usuarios:listar_roles')

def listarProyectoporUsuario(request):
    model=User
    user=User.objects.get(id=request.user.id)
    proyectos=user.equipo.all()
    return render(request, 'proyectos/listarporusuario.html', {'proyectos':proyectos})