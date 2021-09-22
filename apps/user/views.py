from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import Permission, Group
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from apps.user.models import User, Rol
from apps.user.forms import UserForm, PermsForm, RolForm, GroupForm
from apps.login.models import ListaPermitidos
from apps.proyectos.models import RolProyecto, Proyec

class Inicio(LoginRequiredMixin, TemplateView):
    """Retorna al template_name si esta si esta autenticado"""
    template_name = 'inicio.html'


def logout_Usuario(request):
    logout(request)
    return HttpResponseRedirect('/')


class ListarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    """ Vista basada en clase, se utiliza para listar todos los usuarios del sistema



      Argumentos:
      LoginYSuperStaffMixin: verifica que el usuario esté autenticado
      y valida si puede ingresar al sitio de administracion
      ValidarPermisosMixin: valida que tenga los permisos requeridos

      """
    model = User
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'user/listar_usuario.html'
    queryset = User.objects.all()


class ActivosUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    """ Vista basada en clase, se utiliza para listar los usuarios activos del sistema"""
    model = User
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'user/listar_userActivos.html'
    queryset = User.objects.filter(is_active=True)


class ActualizaUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = User
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'user/actualizar_usuario.html'
    form_class = UserForm
    success_url = reverse_lazy('usuarios:listar_usuario')

class EliminarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    """ Vista basada en clase, se utiliza para desactivar a los usuarios del sistema"""
    model = User
    model2 = ListaPermitidos
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')

    def post(self,request,pk,*args,**kwargs):#Eliminacion logica
        object = User.objects.get(id = pk)
        object2 = ListaPermitidos.objects.get(correo=object.email)
        object.delete()
        object2.delete()
        return redirect('usuarios:listar_usuario')

class ListarPermisos(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    """ Vista basada en clase, se utiliza para listar los permisos del sistema"""
    permisos = Permission
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    template_name = 'user/listar_permisos.html'
    queryset = permisos.objects.all().order_by('id')

class CrearPermisos(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase, se utiliza para crear permisos"""
    model = Permission
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    form_class = PermsForm
    template_name = 'user/crear_permisos.html'
    success_url = reverse_lazy('usuarios:listar_permisos')


class ListarRoles(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    """Vista basada en clases para listar los roles de un proyecto"""

    roles = Rol
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    template_name = 'user/listar_roles.html'

    def get(self, request, pk, *args, **kwargs):
        """Funcion para listar los roles de un proyecto dado

        Argumentos:
            request: request
            pk: id del proyecto

        Retorna:
            render de la vista de listado de roles del proyecto
        """

        rolesProyecto = RolProyecto.objects.filter(proyecto_id=pk)
        return render(request, 'user/listar_roles.html',{'object_list':rolesProyecto})


class AsignarRolUserProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase para asignar un rol a un usuario en un proyecto"""



    model = User
    form_class = UserForm
    template_name = 'user/asignar_rol_proyecto.html'

    def get_context_data(self, **kwargs):
        """Funcion para agregar al context el user, el proyectoo_id y los roles
        para poder utilizar en el template asignar_rol_usuario.html

        Retorna:
            context: el contexto
        """


        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        context['proyecto_id'] = self.kwargs.get('pl')
        roles = list(RolProyecto.objects.filter(proyecto_id=context['proyecto_id']))
        context['roles'] = roles
        return context

    def post(self, request, *args, **kwargs):
        """Funcion para trabajar con los datos devueltos por el form

        Se obtiene el user en cuestion, luego se verifica si ya tiene un rol en el
        proyecto actual. Si ha seleccionado un rol, se continua, sino se redirije
        a la lista de roles, luego si ya tiene se borra la actual, luego se añade la nueva.
        """


        proyecto_id = request.POST['proyecto_id']
        user_id = request.POST['usuario_id']
        rol_id = request.POST['rol_id']

        if rol_id:
            user = User.objects.get(id=user_id)
            rol = user.rol.filter(proyecto_id=proyecto_id).first()
            rolProyecto = RolProyecto.objects.get(rol_id=rol_id, proyecto_id=proyecto_id)
            print(user.rol.all())
            if rol:
                user.rol.remove(rol)
            user.rol.add(rolProyecto)
        return redirect('proyectos:listar_integrantes', proyecto_id)



class CrearRoles(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """ Crea un rol, y lo relaciona con el proyecto actual. Es decir, crea un rol para un proyecto """


    model = Rol
    permission_required = ('auth.view_rol', 'auth.add_rol',
                           'auth.delete_rol', 'auth.change_rol')
    form_class = RolForm
    template_name = 'user/crear_rol.html'

    def post(self, request, *args, **kwargs):
        """ Funcion para crear un rol con los datos devueltos por el form

        Crea un nuevo rol con los datos devueltos por el form. Tambien relaciona dicho rol
        con el proyecto actual.
        """


        id = request.path.split('/')[-1]
        nombreProyecto = Proyec.objects.get(id=id).nombre
        nombreRol = request.POST['rol']
        rol = Rol(rol = nombreRol)
        rol.save()
        rolProyecto = RolProyecto(rol_id=rol.id, proyecto_id=id, nombre = f'{nombreRol}-{nombreProyecto}')
        rolProyecto.save()
        return redirect('usuarios:listar_roles', id)

class AgregarPermisosAlRol(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    """docstring for AgregarPermisosAlRol."""
    model = Group
    permission_required = ('auth.view_rol', 'auth.add_rol',
                           'auth.delete_rol', 'auth.change_rol', 'auth.view_permission', 'auth.add_permission',
                            'auth.change_permission')
    form_class = GroupForm
    template_name = 'user/agregar_permisos_roles.html'
    success_url = reverse_lazy('usuarios:listar_roles')



def listarProyectoporUsuario(request):
    """ Función que retorna los proyectos por usuarios"""
    proyectos = request.user.equipo.all()
    return render(request, 'proyectos/listarporusuario.html', {'proyectos':proyectos})