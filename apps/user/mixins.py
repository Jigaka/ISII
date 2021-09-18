from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy

class LoginYSuperStaffMixin(object):

    def dispatch(self, request, *args, **kwargs):
        """ Función que verifica que el usuario esté autenticado y valida si puede ingresar al sitio de administracion"""
        if request.user.is_authenticated:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')


class ValidarPermisosMixin(object):
    permission_required = ''
    url_redirect = None

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
        """ Función que verifica si tiene los permisos, si los tiene continua la ejecución,
        si no los tiene redirecciona a URL_REDIRECT llamando a la Función get_url_redirect"""
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect(self.get_url_redirect())