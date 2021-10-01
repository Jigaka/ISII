from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import Permission,Group
from django.urls import reverse_lazy
from apps.proyectos.models import RolProyecto
from apps.sprint.models import HistoriaUsuario

class LoginYSuperStaffMixin(object):

    def dispatch(self, request, *args, **kwargs):
        """ Función que verifica que el usuario esté autenticado y valida si puede ingresar al sitio de administracion"""
        if request.user.is_authenticated:
                return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No estas autenticado en el sistema.')
        return redirect('index')

class LoginYSuperUser(object):

    def dispatch(self, request, *args, **kwargs):
        """ Función que verifica que el sea super user"""
        if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, 'No tienes permisos para realizar esta acción.')
            return redirect('index')

class LoginNOTSuperUser(object):

    def dispatch(self, request, *args, **kwargs):
        """ Función que verifica que el usuario no sea super user"""
        if not request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, 'No tienes permisos para realizar esta acción.')
            return redirect('index')

class ValidarPermisosMixin(object):
    permission_required = ''
    url_redirect = None

    print("############################### MIXINS ###################3")

    def get_perms(self):
        """ Función que retorna una tupla de los permisos requeridos"""
        if isinstance(self.permission_required,str): return (self.permission_required)
        else: return self.permission_required

    def get_url_redirect(self):
        """ Función que retorna a la ruta que se indicó en URL_REDIRECT, si no especificó la ruta retorna a INICIO"""
        if self.url_redirect is None:
            return reverse_lazy('inicio')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        #request = get_current_request()
        """ Función que verifica
            primero vesrifica que el usuario tenga algún rol asociado, si no tiene se rechaza la acción y
            redirecciona a URL_REDIRECT llamando a la Función get_url_redirect.
            Luego verifica si el rol que tiene el usuario en ese proyecto tiene los permisos necesarios para continuar con la acción,
            si tiene los permisos continua la ejecución, si no los tiene redirecciona a URL_REDIRECT llamando a la Función get_url_redirect
        """
        if request.user.is_superuser: #Si es super user ignora los permisos requeridos, quitar al if para restringir por roles y no exista un super user
            return super().dispatch(request, *args, **kwargs)

        print("Request",request)
        print("ID user",request.user.id)
        print("Request",Group.objects.filter(user=request.user.id).first())
        print("self",self)
        print("args",args)
        print("kwargs",kwargs)


        tiene_grupo = Group.objects.filter(user=request.user.id).first() # se trae los grupos del usuario, si no tiene es None
        print("TIENE GRUPO ",tiene_grupo)

        if tiene_grupo == None: # se verifica que tenga un rol asociado
            messages.error(request, 'No tienes ningun rol asociado.')
            return redirect(self.get_url_redirect())
        else: # en caso que los tenga, se busca obtener el id del proyecto
            if len(kwargs) == 2:
                rol = request.user.rol.filter(proyecto_id=kwargs['pl']).first() #en pl esta el id del proyecto em pk debe venir el id del usuario
                print(len(kwargs))
            else:
                rol = request.user.rol.filter(proyecto_id=kwargs['pk']).first()
                print(len(kwargs))
            print("Rol", rol)
            if rol == None: # Si no tiene rol en ese proyecto se rechaza la acción
                messages.error(request, 'No tienes rol en este proyecto.')
                return redirect(self.get_url_redirect())

            print(len(kwargs))
            grupo =  Group.objects.filter(name=rol.nombre).first()
            print("GRUPO",grupo)
            print("Rol", rol)
            perms = self.get_perms()
            print(perms)
            print(grupo)
            print(grupo.permissions.all())

            for permisos in perms: #Se verifica que el rol tenga los permiso necesarios
                print("PERMISOS", permisos)
                print(grupo.permissions.filter(codename=permisos).all())
                print("GRUPO PERMISOS ", grupo.permissions.filter(codename=permisos))
                if not grupo.permissions.filter(codename=permisos).exists():
                    messages.error(request, 'No tienes permisos para realizar esta acción.')
                    return redirect(self.get_url_redirect())
            return super().dispatch(request, *args, **kwargs)
            messages.error(request, 'No tienes permisos para realizar esta acción.')
            return redirect(self.get_url_redirect())


class ValidarPermisosMixinPermisos(object):
    """Esta clase se llama para acciones especiales"""
    permission_required = ''
    url_redirect = None
    print("############################### MIXINS 2 ###################3")
    def get_perms(self):
        """ Función que retorna una tupla de los permisos requeridos"""
        if isinstance(self.permission_required,str): return (self.permission_required)
        else: return self.permission_required

    def get_url_redirect(self):
        """ Función que retorna a la ruta que se indicó en URL_REDIRECT, si no especificó la ruta retorna a INICIO"""
        if self.url_redirect is None:
            return reverse_lazy('inicio')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        """ Función que verifica
            primero vesrifica que el usuario tenga algún rol asociado, si no tiene se rechaza la acción y
            redirecciona a URL_REDIRECT llamando a la Función get_url_redirect.
            Luego verifica si el rol que tiene el usuario en ese proyecto tiene los permisos necesarios para continuar con la acción,
            si tiene los permisos continua la ejecución, si no los tiene redirecciona a URL_REDIRECT llamando a la Función get_url_redirect
        """
        if request.user.is_superuser: #Si es super user ignora los permisos requeridos, quitar al if para restringir por roles y no exista un super user
            return super().dispatch(request, *args, **kwargs)
        print("self",self)
        print("Request path",request.path)


        print("args",args)
        print("kwargs",kwargs['pk'])
        tiene_grupo = Group.objects.filter(user=request.user.id).first() # se trae los grupos del usuario, si no tiene es None
        print("TIENE GRUPO ",tiene_grupo)


        if tiene_grupo == None: # se verifica que tenga un rol asociado
            messages.error(request, 'No tienes ningun rol asociado.')
            return redirect(self.get_url_redirect())
        else:

            #if request.path.find("agregar_permisos_roles") or request.path.find("eliminar_rol"):
            print("DEBES ESTAR AQUI")
            print("Request PWTH",request.path)
            print("ROL USUARIOOO A MODIFICAR",request.user.rol.filter(id = kwargs['pk']))
            #rolProyecto = RolProyecto.objects.get(rol_id=kwargs['pk'])
            rolProyecto = RolProyecto.objects.get(rol_id=kwargs['pk'])
            id_proyecto = rolProyecto.proyecto_id
            print("rolProyecto2",rolProyecto)
            print("IDProyecto2",id_proyecto)

            #elif request.path.find("editar_us") or request.path.find("aprobar_us") or request.path.find("eliminar_us"):
            #    print("Request PWTH",request.path)
            #    print("QUE HACES AQUI")
                #print("HistoriaUsuario",HistoriaUsuario.objects.get(id=kwargs['pk']))
            #    id_proyecto = HistoriaUsuario.objects.get(id=kwargs['pk']).proyecto.id #id del proyecto se obtiene por us
                #self.url_redirect = '/../proyectos/ver_proyecto/' + str(id_proyecto)


            rol = request.user.rol.filter(proyecto_id=id_proyecto).first()
            print("ROL USUARIOOO QUE MODIFICA", rol)
            grupo =  Group.objects.filter(name=rol.rol).first()
            #path = request.path.rsplit('/', 2)[0]
            #print("PATHHHH",path)
            perms = self.get_perms()
            print(perms)
            print(grupo)
            print(grupo.permissions.all())
            for permisos in perms:#Se verifica que el rol tenga los permiso necesarios
                print("PERMISOS", permisos)
                print(grupo.permissions.filter(codename=permisos).all())
                print("GRUPO PERMISOS ", grupo.permissions.filter(codename=permisos))
                if not grupo.permissions.filter(codename=permisos).exists():
                    messages.error(request, 'No tienes permisos para realizar esta acción.')
                    return redirect(self.get_url_redirect())
            return super().dispatch(request, *args, **kwargs)
            messages.error(request, 'No tienes permisos para realizar esta acción.')
            return redirect(self.get_url_redirect())

class ValidarPermisosMixinHistoriaUsuario(object):
    """Esta clase se llama para acciones especiales"""
    permission_required = ''
    url_redirect = None
    print("############################### MIXINS 3 ###################3")
    def get_perms(self):
        """ Función que retorna una tupla de los permisos requeridos"""
        if isinstance(self.permission_required,str): return (self.permission_required)
        else: return self.permission_required

    def get_url_redirect(self):
        """ Función que retorna a la ruta que se indicó en URL_REDIRECT, si no especificó la ruta retorna a INICIO"""
        if self.url_redirect is None:
            return reverse_lazy('inicio')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        #request = get_current_request()
        """ Función que verifica si tiene los permisos, si los tiene continua la ejecución,
        si no los tiene redirecciona a URL_REDIRECT llamando a la Función get_url_redirect"""
        if request.user.is_superuser: #Si es super user ignora los permisos requeridos, quitar al if para restringir por roles y no exista un super user
            return super().dispatch(request, *args, **kwargs)

        tiene_grupo = Group.objects.filter(user=request.user.id).first() # se trae los grupos del usuario, si no tiene es None
        print("TIENE GRUPO ",tiene_grupo)

        if tiene_grupo == None: # se verifica que tenga un rol asociado
            messages.error(request, 'No tienes ningun rol asociado.')
            return redirect(self.get_url_redirect())
        else:
            request.path.find("editar_us") or request.path.find("aprobar_us") or request.path.find("eliminar_us")
            print("Request PWTH",request.path)
            print("QUE HACES AQUI")
            #print("HistoriaUsuario",HistoriaUsuario.objects.get(id=kwargs['pk']))
            id_proyecto = HistoriaUsuario.objects.get(id=kwargs['pk']).proyecto.id #id del proyecto se obtiene por us
            #self.url_redirect = '/../proyectos/ver_proyecto/' + str(id_proyecto)
            rol = request.user.rol.filter(proyecto_id=id_proyecto).first()
            print("ROL USUARIOOO QUE MODIFICA", rol)
            grupo =  Group.objects.filter(name=rol.rol).first()
            #path = request.path.rsplit('/', 2)[0]
            #print("PATHHHH",path)
            perms = self.get_perms()
            print(perms)
            print(grupo)
            print(grupo.permissions.all())
            for permisos in perms:#Se verifica que el rol tenga los permiso necesarios
                print("PERMISOS", permisos)
                print(grupo.permissions.filter(codename=permisos).all())
                print("GRUPO PERMISOS ", grupo.permissions.filter(codename=permisos))
                if not grupo.permissions.filter(codename=permisos).exists():
                    messages.error(request, 'No tienes permisos para realizar esta acción.')
                    return redirect(self.get_url_redirect())
            return super().dispatch(request, *args, **kwargs)
            messages.error(request, 'No tienes permisos para realizar esta acción.')
            return redirect(self.get_url_redirect())
