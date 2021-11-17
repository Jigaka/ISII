from django.shortcuts import redirect, render
from django.contrib.auth.models import  Group
from django.template.loader import get_template
from .forms import ProyectoForm, configurarUSform, editarProyect, CrearUSForm,aprobar_usform, estimar_userform, reasinarUSform, rechazar_usform, cambiarEstadoProyect, asignarEquipoProyect
from .models import Proyec
from apps.sprint.models import HistoriaUsuario, Sprint, Historial_HU, Estado_HU
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginYSuperUser, LoginNOTSuperUser, ValidarPermisosMixinPermisos, ValidarPermisosMixinHistoriaUsuario, ValidarPermisosMixinSprint
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from apps.user.models import User, Rol
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail

'''
Funcion para crear un proyecto.
En request, se se obtiene todos los parametros del usuario actual
Se devuelve un form para crear un proyecto y guardar en la base de datos.
'''
class CrearProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase, se utiliza para crear permisos"""
    model = Proyec
    permission_required = ('auth.view_permission', 'auth.add_permission',
                           'auth.delete_permission', 'auth.change_permission')
    form_class = ProyectoForm
    template_name = 'proyectos/crear_proyecto.html'
    success_url = reverse_lazy('proyectos:listar_proyectos')




class ListarProyectos(LoginYSuperStaffMixin, LoginYSuperUser, ListView):
    """Vista basada en clase para mostrar todos los proyectos para el admin"""


    model = Proyec
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    template_name = 'proyectos/listar_proyectos.html'
    queryset = Proyec.objects.all()



'''
Funcion para editar un proyecto.
En request, se se obtiene todos los parametros del usuario actual.
El id representa el id del proyecto a editar
Se devuelve un form para editar un proyecto y actualizar en la base de datos.
'''

class EditarProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = Proyec
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/editar_proyecto.html'
    form_class = editarProyect
    success_url = reverse_lazy('proyectos:mis_proyectos')

'''
Función para modificar el estado del proyecto
'''
class cambiarEstadoProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Proyec
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/cambiar_estado_proyecto.html'
    form_class = cambiarEstadoProyect
    success_url = reverse_lazy('proyectos:mis_proyectos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_proyecto = self.kwargs['pk']
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

'''
Función para asignar euqipo al proyecto
'''
class asignarEquipoProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Proyec
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/asignar_equipo_proyecto.html'
    form_class = asignarEquipoProyect
    def get_success_url(self):
        id = self.object.pk
        proyecto = Proyec.objects.get(id=id)
        for x in proyecto.equipo.all():
            user = User.objects.get(id=x.id)
            context = {'proyecto': proyecto}
            template = get_template('correos/equipo.html')
            content = template.render(context)
            email = EmailMultiAlternatives('Notificacion Apepu Gestor', 'Notificacion', settings.EMAIL_HOST_USER, [user.getEmail()])
            email.attach_alternative(content, 'text/html')
            email.send()
        return reverse('proyectos:mis_proyectos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_proyecto = self.kwargs['pk']
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

'''
Funcion para eliminar un proyecto.
En request, se se obtiene todos los parametros del usuario actual.
El id representa el id del proyecto a eliminar
Se devuelve un form para confirmar la eliminacion del proyecto.
'''
class EliminarProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    """ Vista basada en clase, se utiliza para eliminar un proyecto"""
    model = Proyec
    permission_required = ('user.view_user', 'user.add_user',
                           'user.delete_user', 'user.change_user')
    def post(self,request,pk,*args,**kwargs):#Eliminacion logica
        object = Proyec.objects.get(id = pk)
        object.delete()
        return redirect('proyectos:listar_proyectos')

class Proyecto(LoginYSuperStaffMixin, ValidarPermisosMixin,TemplateView):
    # permission_required = ('user.view_user', 'user.add_user',
    #                        'user.delete_user', 'user.change_user')
    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyec.objects.get(id=pk)
        return render(request, 'proyectos/proyecto.html', {'proyecto':proyecto, 'proyecto_id':pk})

class ListadoIntegrantes(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    ''' Vista basada en clase, muestra los integrantes de un proyecto'''

    model = User
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get(self, request, pk, *args, **kwargs):
        """ Funcion para retornar la lista de integrantes de un proyecto
        Argumentos:
            pk: ID del proyecto
        Returns:
            view: render listado de integrantes
        """
        users = Proyec.objects.get(id=pk).equipo.all()
        ''' Doc para la linea de abajo
            Esta parte es un poco larga.
            Recorre la lista users, para obtener cada user. Luego, de acuerdo al user,obtiene
            su rol dentro del proyecto con el id=pk.
            Para obtener el rol del user, primero trae filtra el rol del user respecto al proyecto,
            ahi se obtiene el id del rol. Con el id del rol, se obtiene el rol del modelo Rol.
        '''
        integrantes = [{'user':user, 'rol': Rol.objects.filter(id = user.rol.filter(proyecto_id=pk).first().rol.id if user.rol.filter(proyecto_id=pk).first() else None ).first()} for user in users]
        proyecto = Proyec.objects.get(id=pk)
        return render(request, 'proyectos/listar_integrantes.html', {'users': integrantes, 'proyecto': proyecto})

class ExpulsarIntegrantes(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase se utiliza para expulsar un integrante del proyecto"""

    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    model = Proyec
    print("ExpulsarIntegrantes")
    fields = '__all__'
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id = kwargs['pk'])
        proyecto = Proyec.objects.get(id=kwargs['pl'])
        context = {'proyecto': proyecto}
        template = get_template('correos/expulsar.html')
        content = template.render(context)
        email = EmailMultiAlternatives('Notificacion Apepu Gestor', 'Notificacion', settings.EMAIL_HOST_USER,
                                       [user.getEmail()])
        email.attach_alternative(content, 'text/html')
        email.send()
        rol = user.rol.filter(proyecto_id=kwargs['pl']).first()
        if rol == None:
            proyecto.equipo.remove(user)
            return redirect('proyectos:listar_integrantes', kwargs['pl'])
        grupo =  Group.objects.filter(name=rol.nombre).first()
        proyecto.equipo.remove(user)
        user.groups.remove(grupo)
        user.rol.remove(rol)
        return redirect('proyectos:listar_integrantes', kwargs['pl'])

#class listarporencargado( ValidarPermisosMixin, ListView):
#    model = Proyec Clase No usada???
class AsignarRolProyecto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    """Vista basada en clase, se utiliza para asignar un rol a un proyecto"""
    model = Proyec
    permission_required = ('view_permission', 'add_permission',
                           'delete_permission', 'change_permission')
    form_class = ProyectoForm
    template_name = 'proyectos/asignar_rol.html'
    success_url = reverse_lazy('proyectos:listar_proyectos')

def listarProyectoporEncargado(request):
    user = User.objects.get(id=request.user.id)
    proyectos = user.encargado.all()
    return render(request, 'proyectos/listarporencargado.html', {'proyectos': proyectos})
class listarProyectosUsuario(LoginYSuperStaffMixin, ListView):
    """Vista basada en clase para listar los proyectos en los que se esta
    ya sea como encargado o solo miembro.
    """
    model = Proyec
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        proyectos = user.equipo.all()
        return render(request, 'proyectos/listar_proyectos.html', {'object_list': proyectos,'title':'Mis proyectos'})
class CrearUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixin, CreateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    permission_required = ('view_historiausuario', 'add_historiausuario',
                            'delete_historiausuario', 'change_historiausuario')
    model = HistoriaUsuario
    form_class = CrearUSForm
    template_name = 'proyectos/crear_US.html'
    success_url = reverse_lazy('proyectos:listar_us')
    def post(self, request, *args, **kwargs):
        """ Funcion para crear un rol con los datos devueltos por el form
        Crea un nuevo rol con los datos devueltos por el form. Tambien relaciona dicho rol
        con el proyecto actual.
        """
        id = request.path.split('/')[-1]
        proyecto = Proyec.objects.get(id=id)
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        prioridad=request.POST['prioridad']
        user = User.objects.get(id=request.user.id)
        us=HistoriaUsuario(nombre=nombre, descripcion=descripcion,prioridad=prioridad,proyecto=proyecto, product_owner=user)
        us.save()
        id_hu=HistoriaUsuario.objects.get(nombre=nombre).id
        Historial_HU.objects.create(descripcion='Creacion de la Historia de Usuario: '+nombre+' id #'+ id_hu.__str__()+' con prioridad: '+prioridad, hu=HistoriaUsuario.objects.get(id=id_hu))
        return redirect('proyectos:listar_us', id)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        context['proyecto'] = Proyec.objects.get(id=pk)
        return context

class ConfigurarUs(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/configurar_us.html'
    form_class = configurarUSform
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #pk = self.kwargs['pk']
        id_hu = self.object.pk
        id_proyecto = HistoriaUsuario.objects.get(id=id_hu).proyecto.id
        id_sprint = HistoriaUsuario.objects.get(id=id_hu).sprint.id
        #print(id_proyecto)
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        context['sprint'] = Sprint.objects.get(id=id_sprint)
        return context
    def get_success_url(self):
        id_hu = self.object.pk
        idp = HistoriaUsuario.objects.get( id=id_hu).asignacion.id
        user = User.objects.get(id=idp)
        context = {'hu': HistoriaUsuario.objects.get(id=id_hu)}
        template = get_template('correos/asignacion.html')
        content = template.render(context)
        email = EmailMultiAlternatives('Notificacion Apepu Gestor', 'Notificacion', settings.EMAIL_HOST_USER, [user.getEmail()])
        email.attach_alternative(content, 'text/html')
        email.send()
        template = get_template('correos/estimar_desarrollador.html')
        content = template.render(context)
        email = EmailMultiAlternatives('Notificacion Apepu Gestor', 'Notificacion', settings.EMAIL_HOST_USER, [user.getEmail()])
        email.attach_alternative(content, 'text/html')
        email.send()
        Historial_HU.objects.create(descripcion='Asignacion de la Historia de Usuario a: ' + HistoriaUsuario.objects.get( id=id_hu).asignacion.__str__(), hu=HistoriaUsuario.objects.get(id=id_hu))
        Historial_HU.objects.create(descripcion=' Estmacion del Scum Master: ' + HistoriaUsuario.objects.get(id=id_hu).estimacion_scrum.__str__(), hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('sprint:ver_sb', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id})

class Reasignar_us(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'sprint/reasingar_us.html'
    form_class = reasinarUSform
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        id_hu = self.object.pk
        #print("REASIGNAR",HistoriaUsuario.objects.get(id=id_hu).sprint.id)
        id_proyecto = HistoriaUsuario.objects.get(id=id_hu).proyecto.id
        id_sprint = HistoriaUsuario.objects.get(id=id_hu).sprint.id #Se envia en el context tambien el sprint para que no haya error de id
        #print(id_proyecto)
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        context['sprint'] = Sprint.objects.get(id=id_sprint)
        return context
    def get_success_url(self):
        id_hu = self.object.pk
        idp = HistoriaUsuario.objects.get(id=id_hu).asignacion.id
        user = User.objects.get(id=idp)
        context = {'hu': HistoriaUsuario.objects.get(id=id_hu)}
        template = get_template('correos/asignacion.html')
        content = template.render(context)
        email = EmailMultiAlternatives('Notificacion Apepu Gestor', 'Notificacion', settings.EMAIL_HOST_USER,
                                       [user.getEmail()])
        email.attach_alternative(content, 'text/html')
        email.send()
        Historial_HU.objects.create(
            descripcion='Reasignacion de la Historia de Usuario a: ' + HistoriaUsuario.objects.get(
                id=id_hu).asignacion.__str__(), hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('sprint:ver_sb', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id})
class EditarUs(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para editar las historias de usuarios del proyecto"""
    model = HistoriaUsuario
    #permission_required = ('view_rol', 'add_rol',
    #                       'delete_rol', 'change_rol')
    permission_required = ('view_historiausuario', 'add_historiausuario',
                            'delete_historiausuario', 'change_historiausuario')
    template_name = 'proyectos/editar_us.html'
    form_class = CrearUSForm
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        print(pk)
        id_hu = self.object.pk
        id_proyecto = HistoriaUsuario.objects.get(id=id_hu).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context
    def form_valid(self, form):
        form.instance.rechazado_PB = False
        return super(EditarUs, self).form_valid(form)
    def get_success_url(self):
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })
class ListarUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixin, ListView):
    """ Vista basada en clase, se utiliza para listar las historias de usuarios del sistema del proyecto"""
    model = HistoriaUsuario
    template_name = 'proyectos/listar_us.html'
    permission_required = ('view_historiausuario', 'delete_historiausuario')

    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyec.objects.get(id=pk)
        us = proyecto.proyecto.filter(aprobado_PB=False).order_by('-prioridad_numerica','id')
        return render(request, 'proyectos/listar_us.html', {'proyecto':proyecto, 'object_list': us})
class EliminarUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario,DeleteView):
    """ Vista basada en clase, se utiliza para eliminar un proyecto"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get_success_url(self):
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })

class aprobarUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario,UpdateView ):
    """ Vista basada en clase, se utiliza para aprobar las Historia de Usuario"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/aprobar_us.html'
    form_class = aprobar_usform
    def post(self, request, *args, **kwargs):
        id = request.path.split('/')[-1]
        aprobado_PB=request.POST['aprobado_PB']
        if aprobado_PB== 'on' or aprobado_PB== True:
            HistoriaUsuario.objects.filter(id=id).update(aprobado_PB=True)
            '''envio de email para notificacion '''
            idp = HistoriaUsuario.objects.get(id=id).product_owner.id
            user = User.objects.get(id=idp)
            context = {'hu': HistoriaUsuario.objects.get(id=id)}
            template = get_template('correos/aprobado_pb_correo.html')
            content = template.render(context)
            email = EmailMultiAlternatives('Notificacion Apepu Gestor', 'Notificacion', settings.EMAIL_HOST_USER,
                                           [user.getEmail()])
            email.attach_alternative(content, 'text/html')
            email.send()
        else:
            HistoriaUsuario.objects.filter(id=id).update(aprobado_PB=False)
        return redirect('proyectos:listar_us', HistoriaUsuario.objects.get(id=id).proyecto.id)
    def form_valid(self, form):
        form.instance.rechazado_PB = False
        return super(aprobarUS, self).form_valid(form)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        print(pk)
        id_hu = self.object.pk
        id_proyecto = HistoriaUsuario.objects.get(id=id_hu).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context
    def get_success_url(self):
        id_hu = self.object.pk
        Historial_HU.objects.create(
            descripcion='La Historia de Usuario: ' + HistoriaUsuario.objects.get(
                id=id_hu).nombre+' es aprobada por el Scum Master y pasa al Product Backlog ', hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })

class rechazarUS(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario,UpdateView ):
    """ Vista basada en clase, se utiliza para aprobar las Historia de Usuario"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/rechazar_us.html'
    form_class = rechazar_usform
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        print(pk)
        id_hu = self.object.pk
        id_proyecto = HistoriaUsuario.objects.get(id=id_hu).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context
    def get_success_url(self):
        id_hu = self.object.pk
        hu = HistoriaUsuario.objects.get(id=id_hu)
        idp = hu.product_owner.id
        user = User.objects.get(id=idp)
        context = {'hu': HistoriaUsuario.objects.get(id=id_hu)}
        template = get_template('correos/rechazado.html')
        content = template.render(context)
        email = EmailMultiAlternatives('Notificacion Apepu Gestor', 'Notificacion', settings.EMAIL_HOST_USER,
                                       [user.getEmail()])
        email.attach_alternative(content, 'text/html')
        email.send()
        Historial_HU.objects.create(descripcion='La Historia de Usuario: ' + HistoriaUsuario.objects.get(id=id_hu).nombre + ' es rechazada por el Scrum Master',
            hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('proyectos:listar_us', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id})

class ProductBacklog(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixin, ListView):
    model = HistoriaUsuario
    template_name = 'proyectos/ver_PB.html'
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get(self, request, pk, *args, **kwargs):
        proyecto=Proyec.objects.get(id=pk)
        us = proyecto.proyecto.exclude(aprobado_PB=False).order_by('-prioridad_numerica')
        return render(request, 'proyectos/ver_PB.html', {'object_list': us,'proyecto':proyecto})

class Listar_us_a_estimar(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinSprint, ListView):
    """Vista basada en clase, se utiliza para listar las historia de usuario asignados al developer"""
    model = HistoriaUsuario
    template_name = 'sprint/us-a-estimar.html'
    permission_required = ('view_proyec', 'change_proyec')
    def get(self, request, pk, *args, **kwargs):
        sprint =Sprint.objects.get(id=pk)
        user = User.objects.get(id=request.user.id)
        us = sprint.sprint.filter(asignacion=user, sprint_backlog=True, estimacion=0)
        id_proyecto = Sprint.objects.get(id=pk).proyecto.id
        proyecto = Proyec.objects.get(id=id_proyecto)
        return render(request, 'sprint/us-a-estimar.html', {'object_list': us, 'proyecto': proyecto})

class estimarUS( UpdateView):
    """ Vista basada en clase, se utiliza para que el developer estime su historia de usuario asignado"""
    model = HistoriaUsuario
    #permission_required = ('view_proyec', 'change_proyec')
    template_name = 'sprint/estimar_us.html'
    form_class = estimar_userform
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        print(pk)
        print(self.object.pk)
        id_proyecto = HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id
        print(id_proyecto)
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        id_sprint=HistoriaUsuario.objects.get(id=self.object.pk).sprint.id
        context['sprint'] = Sprint.objects.get(id=id_sprint)
        return context
    def get_success_url(self):
        id_hu = self.object.pk
        Historial_HU.objects.create(
            descripcion=' Estmacion del usuario ' + HistoriaUsuario.objects.get(
                id=id_hu).asignacion.getNombreUsuario()+' :' +HistoriaUsuario.objects.get(
                id=id_hu).estimacion_scrum.__str__(), hu=HistoriaUsuario.objects.get(id=id_hu))
        return reverse('sprint:ver_sb', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id })