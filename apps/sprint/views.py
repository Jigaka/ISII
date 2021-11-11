from typing import List
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import CapacidadDiariaEnSprintForm,rechazarQAForm, SprintForm, agregar_hu_form,\
    aprobarQAForm,configurarEquipoSprintform, cambio_estadoHU_form, CrearActividadForm, cancelar_huform
from .models import CapacidadDiariaEnSprint, Proyec,  Sprint, HistoriaUsuario, User, Historial_HU, Actividad,Estado_HU
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy, reverse
from apps.user.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginYSuperUser, \
     LoginNOTSuperUser, ValidarPermisosMixinPermisos, ValidarPermisosMixinHistoriaUsuario, ValidarPermisosMixinSprint, \
    ValidarQuePertenceAlProyecto, ValidarQuePertenceAlProyectoSprint
import pandas as pd
from datetime import date, timedelta


# Create your views here.
class CrearSprint(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixin, CreateView ):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'proyectos/crear_sprint.html'
    model = Sprint
    form_class = SprintForm
    success_url = reverse_lazy('proyectos:listar_proyectos')

    def get_form_kwargs(self):
        kwargs = super(CrearSprint,self).get_form_kwargs()
        self.kwargs['id_sprint']=0
        kwargs.update(self.kwargs)
        return kwargs

    def form_valid(self, form):
        proyecto = get_object_or_404(Proyec, id=self.kwargs['pk'])
        form.instance.proyecto = proyecto
        return super(CrearSprint, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        proyecto = Proyec.objects.get(id=pk)
        context['proyecto'] = proyecto
        context['existe_sprint_pendiente']=Sprint.objects.filter(proyecto=proyecto,estado="Pendiente").exists()
        return context

    def get_success_url(self):
        return reverse('sprint:listar_sprint', kwargs={'pk': Sprint.objects.get(id=self.object.pk).proyecto.id })


class ListarSprint(LoginYSuperStaffMixin, ValidarQuePertenceAlProyecto, LoginNOTSuperUser, ListView ):
    """ Vista basada en clase, se utiliza para listar las historias de usuarios del sistema del proyecto"""
    model = Sprint
    template_name = 'sprint/listar_sprint.html'
    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyec.objects.get(id=pk)
        sprint = proyecto.proyecto_s.all().order_by('fecha_inicio')
        for s in sprint:
            if (s.estado=='Pendiente'):
                if date.today() >= s.fecha_inicio and date.today() <= s.fecha_fin:
                    Sprint.objects.filter(id=s.id).update(estado='Iniciado')
            if (s.estado=='Iniciado' or s.estado=='Pendiente'):
                if date.today() > s.fecha_fin:
                    Sprint.objects.filter(id=s.id).update(estado='Finalizado')
                    hus = Sprint.objects.get(id=s.id).sprint.all()
                    print(hus)
                    for hu in hus:
                        Estado_HU.objects.create(hu=hu, sprint=hu.sprint, estado=hu.estado,
                                                 desarrollador=hu.asignacion.username, prioridad=hu.prioridad,
                                                 PP=hu.estimacion)
                        if hu.estado != 'Done':
                            HistoriaUsuario.objects.filter(id=hu.id).update(sprint_backlog=False, aprobado_PB=True,
                                                                            prioridad='Alta',prioridad_numerica=3 , estimacion_user=0,estimacion_scrum=0, estimacion=0, estado='Pendiente', asignacion=None, sprint=None)
                            Historial_HU.objects.create(
                                descripcion='La Historia de Usuario: ' + HistoriaUsuario.objects.get(
                                    id=hu.id).nombre + ' sin concluir se agrega de nuevo al Product Backlog con prioridad Alta y estado: '+ HistoriaUsuario.objects.get(
                                    id=hu.id).estado,
                                hu=HistoriaUsuario.objects.get(id=hu.id))
                        elif hu.estado == 'Done':
                            HistoriaUsuario.objects.filter(id=hu.id).update(estado='QA')


        return render(request, 'sprint/listar_sprint.html', {'proyecto':proyecto, 'object_list': sprint})

class AgregarHU_sprint(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario, UpdateView):
    """ Vista basada en clase, se utiliza para editar las historias de usuarios del proyecto"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol',
                          'delete_rol', 'change_rol')
    template_name = 'sprint/agregarHU.html'
    form_class = agregar_hu_form

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto = HistoriaUsuario.objects.get(id=pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context
    def get_success_url(self):
        id_hu = self.object.pk
        return reverse('proyectos:ver_pb', kwargs={'pk': HistoriaUsuario.objects.get(id=id_hu).proyecto.id})
    def post(self, request, *args, **kwargs):
        """ Funcion para crear un rol con los datos devueltos por el form

        Crea un nuevo rol con los datos devueltos por el form. Tambien relaciona dicho rol
        con el proyecto actual.
        """
        id = request.path.split('/')[-1]
        HU = HistoriaUsuario.objects.get(id=id)
        sprint = request.POST['sprint']
        HistoriaUsuario.objects.filter(id=id).update(sprint=sprint, sprint_backlog=True, estado='ToDo')
        Historial_HU.objects.create(
            descripcion='Se agrega la Historia de Usuario: ' + HistoriaUsuario.objects.get(
                id=id).nombre+ ' al Sprint: '+ HistoriaUsuario.objects.get(
                id=id).sprint.nombre,
            hu=HistoriaUsuario.objects.get(id=id))
        return redirect('proyectos:ver_pb', HU.proyecto_id)


class EliminarSprint(LoginYSuperStaffMixin, ValidarPermisosMixinSprint, LoginNOTSuperUser, DeleteView):
    """ Vista basada en clase, se utiliza para eliminar un proyecto"""
    model = Sprint
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    def get_success_url(self):
        return reverse('sprint:listar_sprint', kwargs={'pk': Sprint.objects.get(id=self.object.pk).proyecto.id })

class EditarSprint(LoginYSuperStaffMixin, ValidarPermisosMixinSprint, LoginNOTSuperUser, UpdateView):
    """ Vista basada en clase, se utiliza para editar las historias de usuarios del proyecto"""
    model = Sprint
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'sprint/editar_sprint.html'
    form_class = SprintForm

    def get_form_kwargs(self):
        kwargs = super(EditarSprint,self).get_form_kwargs()
        id_sprint=self.kwargs['pk']
        id_proyecto = Sprint.objects.get(id=id_sprint).proyecto.id
        self.kwargs['pk']=id_proyecto
        self.kwargs['id_sprint']=id_sprint
        kwargs.update(self.kwargs)
        return kwargs

    def get_success_url(self):
        return reverse('sprint:listar_sprint', kwargs={'pk': Sprint.objects.get(id=self.object.pk).proyecto.id })

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto= Sprint.objects.get(id=self.object.pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context


class VerSprint(LoginYSuperStaffMixin, ValidarQuePertenceAlProyectoSprint, TemplateView):
    """
        Vista basada en clase para mostrar el menu de un sprint
    """
    permission_required = ('view_proyec', 'change_proyec')

    def get(self, request, *args, **kwargs):
        """
            funcion para renderizar el menu del sprint
        """
        pk = self.kwargs['pk']

        sprint = Sprint.objects.get(id=pk)
        proyecto=sprint.proyecto

        return render(request, 'sprint/sprint.html',{"sprint":sprint,"proyecto":proyecto})


class VerActividad(LoginYSuperStaffMixin, TemplateView):
    """
        Vista basada en clase para mostrar una actividad
    """
    permission_required = ('view_proyec', 'change_proyec')


    def get(self, request, *args, **kwargs):
        """
            funcion para renderizar una actividad
        """
        pk = self.kwargs['pk']

        actividad = Actividad.objects.get(id=pk)

        return render(request, 'sprint/ver_actividad.html', {"actividad": actividad})


class VerUS(LoginYSuperStaffMixin, TemplateView):
    """
        Vista basada en clase para mostrar un user history
    """
    permission_required = ('view_proyec', 'change_proyec')


    def get(self, request, *args, **kwargs):
        """
            funcion para renderizar un user history
        """
        pk = self.kwargs['pk']

        us = HistoriaUsuario.objects.get(id=pk)
        if us.asignacion_id:
            desarrollador = User.objects.get(id = us.asignacion_id)
        else:
            desarrollador = {
                'username' : 'Sin asignar'
            }
        return render(request, 'sprint/ver_us.html', {"us": us, "desarrollador": desarrollador})





class SprintBacklog(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinSprint, ListView):

    model = HistoriaUsuario
    template_name = 'sprint/ver_sb.html'
    #permission_required = ('view_rol', 'add_rol',
    #                       'delete_rol', 'change_rol')
    def get(self, request, pk, *args, **kwargs):
        sprint=Sprint.objects.get(id=pk)
        proyecto=sprint.proyecto
        if sprint.estado=='Finalizado':
            object_list = sprint.estado_sprint.all()
        else:
            object_list = sprint.sprint.all()

        return render(request, 'sprint/ver_sb.html', {'object_list': object_list,'sprint':sprint,'proyecto':proyecto})

class TablaKanban(LoginYSuperStaffMixin, ListView):
    model = HistoriaUsuario
    template_name = 'sprint/ver_sb.html'
    '''permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')'''

    def post(self, request, *args, **kwargs):
        id_uh = request.POST['id']
        estado = request.POST['estado']

        Historial_HU.objects.create(descripcion='Cambio de estado '+HistoriaUsuario.objects.get(id=id_uh).estado_anterior+' a estado '+ estado, hu=HistoriaUsuario.objects.get(id=id_uh))
        HistoriaUsuario.objects.filter(id=id_uh).update(estado=estado, estado_anterior=estado)
        if estado == 'ToDo':
            HistoriaUsuario.objects.filter(id=id_uh).update(fecha_ToDo=date.today())
        elif estado == 'Doing':
            HistoriaUsuario.objects.filter(id=id_uh).update(fecha_Doing=date.today())
        elif estado == 'Done':
            HistoriaUsuario.objects.filter(id=id_uh).update(fecha_Done=date.today())
        elif estado == 'QA':
            HistoriaUsuario.objects.filter(id=id_uh).update(fecha_QA=date.today())
        return JsonResponse({'estado':'ok'})

    def get(self, request, pk, *args, **kwargs):
        sprint=Sprint.objects.get(id=pk)
        id_proyecto = Sprint.objects.get(id=pk).proyecto.id
        proyecto = Proyec.objects.get(id=id_proyecto)
        if sprint.estado != 'Finalizado':
            userHistorys = sprint.sprint.all()
            us = [{'userHistory' : us, 'actividades' : us.actividades.all()} for us in userHistorys]
            return render(request, 'sprint/kanban.html', {'object_list': us, 'sprint': sprint, 'proyecto': proyecto})
        else:
            us=sprint.estado_sprint.all()
            return render(request, 'sprint/kanban-fin.html', {'object_list': us, 'sprint': sprint, 'proyecto': proyecto})


class AddActividad(LoginYSuperStaffMixin, CreateView):
    '''
        Vista para crear una actividad para una historia de usuario
    '''
    template_name = 'sprint/crear_actividad.html'
    form_class = CrearActividadForm
    model = Actividad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        us = self.kwargs['us']
        context['pk'] = pk
        context['us'] = us
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        us = self.kwargs['us']
        nombre = request.POST['nombre']
        comentario = request.POST['comentario']
        hora_trabajo = request.POST['hora_trabajo']
        fecha = request.POST['fecha']
        actividad = Actividad(nombre=nombre, comentario=comentario, hora_trabajo=hora_trabajo, id_sprint=pk, fecha=fecha)
        actividad.save()
        history = HistoriaUsuario.objects.get(id=us)
        history.actividades.add(actividad)
        return redirect('sprint:kanban', pk)

class AprobarQA(LoginYSuperStaffMixin, CreateView):
    '''
        Vista para aprobar  una historia de usuario en QA
    '''
    template_name = 'sprint/aprobarQA.html'
    form_class = aprobarQAForm
    model = HistoriaUsuario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        us = self.kwargs['us']
        context['pk'] = pk
        context['us'] = us
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        us = self.kwargs['us']
        aprobado_QA = request.POST['aprobado_QA']
        comentario = request.POST['comentario']
        if aprobado_QA=='on':
            HistoriaUsuario.objects.get(id=us).estado_hu.update(aprobado_QA=True,comentario=comentario,estado='Aprobado_QA')
            HistoriaUsuario.objects.filter(id=us).update(aprobado_QA=True , comentario=comentario)
            Historial_HU.objects.create(
                 descripcion='La Historia de Usuario: ' + HistoriaUsuario.objects.get(
                id=us).nombre + ' es aprobada. Comentario: '+HistoriaUsuario.objects.get(id=us).comentario,
                 hu=HistoriaUsuario.objects.get(id=us))
        return redirect('sprint:kanban', pk)

class RechazarQA(LoginYSuperStaffMixin, CreateView):
    '''
        Vista para rechazar una historia de usuario en QA
    '''
    template_name = 'sprint/rechazarQA.html'
    form_class = rechazarQAForm
    model = HistoriaUsuario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        us = self.kwargs['us']
        context['pk'] = pk
        context['us'] = us
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        us = self.kwargs['us']
        rechazado_QA = request.POST['rechazado_QA']
        comentario=request.POST['comentario']
        if rechazado_QA == 'on':
            us_copia=HistoriaUsuario.objects.get(id=us).estado_hu.filter(sprint_id=pk).update(rechazado_QA=True, comentario=comentario, estado='Rechazado_QA')
            HistoriaUsuario.objects.filter(id=us).update(sprint_backlog=False, aprobado_PB=True,
                                                            prioridad='Alta', estimacion_user=0, estimacion_scrum=0,
                                                            estimacion=0, estado='Pendiente', asignacion=None,
                                                            sprint=None)
            Historial_HU.objects.create(
                descripcion='La Historia de Usuario: ' + HistoriaUsuario.objects.get(
                    id=us).nombre + ' es rechazada y se agrega de nuevo al Product Backlog con prioridad Alta y estado: Pendiente',
                hu=HistoriaUsuario.objects.get(id=us))
        return redirect('sprint:kanban', pk)


class configurarEquipoSprint(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinSprint, UpdateView):
    """ Vista basada en clase, se utiliza para que el developer estime su historia de usuario asignado"""
    model = Sprint
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'sprint/configurar_equipo.html'
    form_class = configurarEquipoSprintform

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto= Sprint.objects.get(id=self.object.pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

    def get_success_url(self):#HistoriaUsuario.objects.get(id=self.object.pk).sprint.id
        return reverse('sprint:listar_equipo', kwargs={'pk': self.object.pk})

class Cambio_de_estadoHU(LoginYSuperStaffMixin, LoginNOTSuperUser, UpdateView):
    """ Vista basada en clase, se utiliza para que el developer estime su historia de usuario asignado"""
    model = HistoriaUsuario
    #permission_required = ('view_proyec', 'change_proyec')
    template_name = 'sprint/cambio_estado.html'
    form_class = cambio_estadoHU_form

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs['pk']
        print(pk)
        print(self.object.pk)
        id_proyecto =  HistoriaUsuario.objects.get(id=pk).proyecto.id
        id_sprint = HistoriaUsuario.objects.get(id=pk).sprint.id
        context['sprint'] = Sprint.objects.get(id=id_sprint)
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

    def get_success_url(self):#HistoriaUsuario.objects.get(id=self.object.pk).sprint.id
        id_hu=self.object.pk
        Historial_HU.objects.create(descripcion='Cambio de estado ' + HistoriaUsuario.objects.get(
            id=id_hu).estado_anterior + ' a estado ' + HistoriaUsuario.objects.get(
            id=id_hu).estado, hu=HistoriaUsuario.objects.get(id=id_hu))
        if HistoriaUsuario.objects.get(id=id_hu).estado != HistoriaUsuario.objects.get(id=id_hu).estado_anterior:
            if HistoriaUsuario.objects.get(id=id_hu).estado == 'ToDo':
                HistoriaUsuario.objects.filter(id=id_hu).update(fecha_ToDo=date.today(), estado_anterior='ToDo')
            elif HistoriaUsuario.objects.get(id=id_hu).estado == 'Doing':
                HistoriaUsuario.objects.filter(id=id_hu).update(fecha_Doing=date.today(),estado_anterior='Doing')
            elif HistoriaUsuario.objects.get(id=id_hu).estado == 'Done':
                HistoriaUsuario.objects.filter(id=id_hu).update(fecha_Done=date.today(),estado_anterior='Done')
            elif HistoriaUsuario.objects.get(id=id_hu).estado == 'QA':
                HistoriaUsuario.objects.filter(id=id_hu).update(fecha_QA=date.today(), estado_anterior='QA')
        return reverse('sprint:kanban', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).sprint.id})

class ListarEquipo(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarQuePertenceAlProyectoSprint, ListView):
    """Vista basada en clase, se utiliza para listar a los miembros del equipo del sprint"""
    model = Sprint
    template_name = 'sprint/listar_equipo.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        id_proyecto= Sprint.objects.get(id=self.object.pk).proyecto.id
        context['proyecto'] = Proyec.objects.get(id=id_proyecto)
        return context

    def get(self, request, pk, *args, **kwargs):
        sprint = Sprint.objects.get(id=pk)
        equipo = sprint.equipo.all()
        capacidad = CapacidadDiariaEnSprint.objects.filter(sprint=sprint).all()
        id_proyecto = Sprint.objects.get(id=pk).proyecto.id
        proyecto = Proyec.objects.get(id=id_proyecto)
        return render(request, 'sprint/listar_equipo.html', {'sprint':sprint, 'object_list': equipo, 'proyecto': proyecto, 'capacidad': capacidad})

class AsignarCapacidadDiaria(LoginYSuperStaffMixin, LoginNOTSuperUser,CreateView ):
    """ Vista basada en clase, se utiliza para editar los usuarios del sistema"""
    permission_required = ('view_rol', 'add_rol',
                           'delete_rol', 'change_rol')
    template_name = 'sprint/asignar_capacidad.html'
    model = CapacidadDiariaEnSprint
    form_class = CapacidadDiariaEnSprintForm
    success_url = reverse_lazy('inicio.html')

    def form_valid(self, form):
        id_sprint=self.kwargs['pk']
        id_user= self.kwargs['pk2']
        usuario = get_object_or_404(User, id=id_user)
        sprint = get_object_or_404(Sprint, id=id_sprint)
        form.instance.usuario = usuario
        form.instance.sprint = sprint
        return super(AsignarCapacidadDiaria, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk=self.kwargs['pk']
        sprint = Sprint.objects.get(id=pk)
        proyecto=sprint.proyecto

        #users = Sprint.objects.values_list('equipo', flat=True).filter(id=pk)
        #if self.request.user.pk in users:
            #Estoy dentro del equipo de trabajo#
        #    estoyEnEquipo=True
        #else:
            #Estoy fuera del equipo de trabajo#
        #    estoyEnEquipo=False

        context['sprint']=sprint
        context['proyecto'] = proyecto
        id_user= self.kwargs['pk2']
        usuario = get_object_or_404(User, id=id_user)
        context['capacidadCargada']=CapacidadDiariaEnSprint.objects.filter(sprint=sprint,usuario=usuario).exists()
        return context

    def get_success_url(self, **kwargs):
        return reverse('sprint:listar_equipo', kwargs={'pk': CapacidadDiariaEnSprint.objects.get(id=self.object.pk).sprint.id })

class Historial_por_hu(LoginYSuperStaffMixin, LoginNOTSuperUser, ListView):
    """Vista basada en clase, se utiliza para listar las historia de usuario asignados al developer"""
    model = Historial_HU
    template_name = 'sprint/historial_hu.html'
    #permission_required = ('view_proyec', 'change_proyec')

    def get(self, request, pk, *args, **kwargs):
        hu =HistoriaUsuario.objects.get(id=pk)
        historial=hu.historial_hu.all()
        id_proyecto = hu.proyecto.id
        proyecto = Proyec.objects.get(id=id_proyecto)
        return render(request, 'sprint/historial_hu.html', {'object_list': historial, 'proyecto': proyecto})

class VisualizarCapacidad(LoginYSuperStaffMixin, LoginNOTSuperUser, TemplateView):
    """docstring for VisualizarCapacidad."""
    template_name = 'sprint/capacidad.html'

    def get(self, request, pk, *args, **kwargs):
        sprint = Sprint.objects.get(id=pk)
        equipo = sprint.equipo.all()
        capacidad = CapacidadDiariaEnSprint.objects.filter(sprint=sprint).all()
        print(capacidad)
        suma_horas_equipo = 0
        for e in equipo:
            for c in capacidad:
                if e.id == c.usuario.id:
                    suma_horas_equipo += c.capacidad_diaria_horas
        sprint.capacidad_de_equipo_sprint = suma_horas_equipo * sprint.duracion_dias
        print(sprint.capacidad_de_equipo_sprint)
        Sprint.objects.filter(id=pk).update(capacidad_equipo=suma_horas_equipo)
        Sprint.objects.filter(id=pk).update(capacidad_de_equipo_sprint=sprint.capacidad_de_equipo_sprint)
        id_proyecto = Sprint.objects.get(id=pk).proyecto.id
        proyecto = Proyec.objects.get(id=id_proyecto)
        return render(request, 'sprint/capacidad.html', {'sprint': sprint, 'proyecto': proyecto})

class BurnDownChart(TemplateView):
    """Vista basada en clase, se utiliza para listar las historia de usuario asignados al developer"""
    template_name = 'sprint/burn_down_chart3.html'
    model = Actividad

    def get(self, request, *args, **kwargs):
        """
            funcion para renderizar el menu del sprint
        """

        fechas = []
        pk = self.kwargs['pk']
        sprint = Sprint.objects.get(id=pk)
        proyecto=sprint.proyecto
        actividad = Actividad.objects.filter(id_sprint=sprint.id).all().order_by('fecha')
        for a in actividad:
            print(a.fecha)
        fecha_inicio = sprint.fecha_inicio
        fecha_fin = sprint.fecha_fin
        datos = [0]*(sprint.duracion_dias+1)
        print(datos)
        fecha_actual = date.today()
        for f in range(sprint.duracion_dias):
            d = "Day " + str(f+1)
            fechas.append(d)
        dt = pd.bdate_range(start=fecha_inicio, end=fecha_fin)
        horas_disponibles = sprint.capacidad_de_equipo_sprint
        datos[0] = sprint.capacidad_de_equipo_sprint
        dia = 1
        for time in dt:##Debo totalizar las horas de los US por sprint o sea por fecha, dia 1 tantas horas hechas y asi
            for i in actividad:
                if time==i.fecha and dia < (sprint.duracion_dias+1):
                    sprint.capacidad_de_equipo_sprint = sprint.capacidad_de_equipo_sprint-i.hora_trabajo
                    datos[dia] = sprint.capacidad_de_equipo_sprint
                    dia += 1
        dia = 0
        print(datos)
        for i in datos:
            if i == 0:
                datos[dia] = sprint.capacidad_de_equipo_sprint
            dia +=1
        print("Fechas", fechas)
        print(datos)
        return render(request, 'sprint/burn_down_chart3.html',{'sprint': sprint,'proyecto': proyecto, 'datos': datos, 'fechas': fechas})
class Cancelar_hu(LoginYSuperStaffMixin, LoginNOTSuperUser, ValidarPermisosMixinHistoriaUsuario,UpdateView ):
    """ Vista basada en clase, se utiliza para aprobar las Historia de Usuario"""
    model = HistoriaUsuario
    permission_required = ('view_rol', 'add_rol', 'delete_rol', 'change_rol')
    template_name = 'sprint/cancelar_hu.html'
    form_class = cancelar_huform
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
    def post(self, request, *args, **kwargs):
        id = request.path.split('/')[-1]
        cancelado=request.POST['cancelado']
        if cancelado== 'on':
            HistoriaUsuario.objects.filter(id=id).update(cancelado=True, estado='Cancelado')
        else:
            HistoriaUsuario.objects.filter(id=id).update(cancelado=False, estado='Cancelado')
        return redirect('proyectos:ver_pb', HistoriaUsuario.objects.get(id=id).proyecto.id)
    def get_success_url(self):
        return reverse('proyectos:ver_pb', kwargs={'pk': HistoriaUsuario.objects.get(id=self.object.pk).proyecto.id })