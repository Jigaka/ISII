from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import Permission, Group
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, ValidarPermisosMixinPermisos, LoginYSuperUser
from apps.user.models import User, Rol
from apps.user.forms import UserForm, PermsForm, RolForm, GroupForm, ActualizarForm
from apps.login.models import ListaPermitidos
from apps.proyectos.models import RolProyecto, Proyec

class Inicio(LoginRequiredMixin, TemplateView):
    """Retorna al template_name si esta si esta autenticado"""
    template_name = 'inicio.html'


def logout_Usuario(request):
    logout(request)
    return HttpResponseRedirect('/')


class ListarUsuario(LoginYSuperUser, ListView):
    """ Vista basada en clase, se utiliza para listar todos los usuarios del sistema



      Argumentos:
      LoginYSuperStaffMixin: verifica que el usuario esté autenticado
      y valida si puede ingresar al sitio de administracion
      ValidarPermisosMixin: valida que tenga los permisos requeridos

      """
    model = User
    permission_required = ('view_user', 'add_user',
                           'delete_user', 'change_user')
    template_name = 'user/listar_usuario.html'
    queryset = User.objects.all()


class ActivosUsuario(LoginYSuperUser, ListView):
    """ Vista basada en clase, se utiliza para listar los usuarios activos del sistema"""
    model = User
    permission_required = ('view_user', 'add_user',
                           'delete_user', 'change_user')
    template_name = 'user/listar_userActivos.html'
    queryset = User.objects.filter(is_active=True)


class ActualizaUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = User
    permission_required = ('view_user', 'add_user',
                           'delete_user', 'change_user')
    template_name = 'user/actualizar_usuario.html'
    form_class = ActualizarForm

    def get_success_url(self):
        return reverse_lazy('usuarios:listar_usuario')

class EliminarUsuario(LoginYSuperUser, DeleteView):
    """ Vista basada en clase, se utiliza para desactivar a los usuarios del sistema"""
    model = User
    model2 = ListaPermitidos
    permission_required = ('view_user', 'add_user',
                           'delete_user', 'change_user')

    def post(self,request,pk,*args,**kwargs):#Eliminacion logica
        object = User.objects.get(id = pk)
        object2 = ListaPermitidos.objects.get(correo=object.email)
        object.delete()
        object2.delete()
        return redirect('usuarios:listar_usuario')

class ListarPermisos(LoginYSuperUser, ListView):
    """ Vista basada en clase, se utiliza para listar los permisos del sistema"""
    permisos = Permission
    permission_required = ('view_permission', 'add_permission',
                           'delete_permission', 'change_permission')
    template_name = 'user/listar_permisos.html'
    queryset = permisos.objects.all().order_by('id')

class CrearPermisos(LoginYSuperUser, CreateView):
    """Vista basada en clase, se utiliza para crear permisos"""
    model = Permission
    permission_required = ('view_permission', 'add_permission',
                           'delete_permission', 'change_permission')
    form_class = PermsForm
    template_name = 'user/crear_permisos.html'
    success_url = reverse_lazy('usuarios:listar_permisos')


class ListarRoles(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    """Vista basada en clases para listar los roles de un proyecto"""

    roles = Rol
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
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
        proyecto = Proyec.objects.filter(id=pk).first()
        return render(request, 'user/listar_roles.html',{'object_list':rolesProyecto, 'proyecto':proyecto})


class AsignarRolUserProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase para asignar un rol a un usuario en un proyecto"""



    model = User
    form_class = UserForm
    template_name = 'user/asignar_rol_proyecto.html'
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')

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

        proyecto_id = request.POST['proyecto_id']
        user_id = request.POST['usuario_id']
        rol_id = request.POST['rol_id']

        if rol_id:
            user = User.objects.get(id=user_id)
            rol = user.rol.filter(proyecto_id=proyecto_id).first()
            rolProyecto = RolProyecto.objects.get(rol_id=rol_id, proyecto_id=proyecto_id)
            rolProyecto2 = RolProyecto.objects.get(rol_id=rol_id)
            print("rolProyecto2 ",rolProyecto2.proyecto_id)
            print(user.rol.all())
            print("ROLLLL", rol)
            if rol:
                grupo_antiguo = User.objects.filter(id=kwargs['pk']).values('rol__rol__rol').all()
                print("GRUPO ANTIGUO",grupo_antiguo)
                print(self)
                grupo =  Group.objects.filter(name=rol.nombre).first()
                print("GRUPO",grupo)
                user.groups.remove(grupo)
                user.rol.remove(rol)

            user.rol.add(rolProyecto)
            User.save(user, *args, **kwargs)
        return redirect('proyectos:listar_integrantes', proyecto_id)

class EliminarRol(LoginYSuperStaffMixin, ValidarPermisosMixinPermisos, DeleteView):
    """Elimina un rol de un proyecto, y elimina el grupo asociado a ese rol"""
    model = Rol
    model2 = Group
    model3 = RolProyecto
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto = RolProyecto.objects.get(id = pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

    def post(self,request,pk,*args,**kwargs):#Eliminacion logica
        object = Rol.objects.get(id = pk)
        object2 = Group.objects.get(name = object.rol)
        print("Rol a eliminar", object)
        print("Grupo a eliminar", object2)
        print("id pro", RolProyecto.objects.get(id = pk).proyecto.id)
        id_proyecto = RolProyecto.objects.get(id = pk).proyecto.id
        object.delete()
        object2.delete()
        return redirect('usuarios:listar_roles', id_proyecto)



class CrearRoles(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """ Crea un rol, y lo relaciona con el proyecto actual. Es decir, crea un rol para un proyecto """


    model = Rol
    form_class = RolForm
    template_name = 'user/crear_rol.html'
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')

    def get_context_data(self, **kwargs):
        """Funcion para obtener el context, y enviar el proyecto en el template

        Retorna:
            context: el contexto
        """


        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        pk = self.kwargs.get('pk')
        proyecto = Proyec.objects.filter(id=pk).first()
        context['proyecto'] = proyecto
        return context

    def post(self, request, *args, **kwargs):
        """ Funcion para crear un rol con los datos devueltos por el form

        Crea un nuevo rol con los datos devueltos por el form. Tambien relaciona dicho rol
        con el proyecto actual.
        """


        id = request.path.split('/')[-1]
        nombreProyecto = Proyec.objects.get(id=id).nombre
        nombreRol = request.POST['rol']
        rol = Rol(rol = f'{nombreRol}-{nombreProyecto}')
        print("LLAMADA")
        rol.save()
        rolProyecto = RolProyecto(rol_id=rol.id, proyecto_id=id, nombre = f'{nombreRol}-{nombreProyecto}')
        rolProyecto.save()
        print("ROL PROYECTO", rolProyecto)
        #print("ID ROL PROYECTO", rolProyecto.proyecto_id.filter(rol_id=rol.id))
        return redirect('usuarios:listar_roles', id)

class AgregarPermisosAlRol(LoginYSuperStaffMixin, ValidarPermisosMixinPermisos, UpdateView):
    """Agrega permisos al rol"""
    model = Group
    form_class = GroupForm
    template_name = 'user/agregar_permisos_roles.html'
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto = RolProyecto.objects.get(id = pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        context['rol'] = RolProyecto.objects.get(id = pk)
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('usuarios:listar_roles', kwargs={'pk': RolProyecto.objects.get(id=self.object.pk).proyecto.id})



def listarProyectoporUsuario(request):
    """ Función que retorna los proyectos por usuarios"""
    proyectos = request.user.equipo.all()
    return render(request, 'proyectos/listarporusuario.html', {'proyectos':proyectos})
