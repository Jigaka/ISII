import pytest
from django.test import TestCase
from faker import Faker
from ddf import G, F
from apps.proyectos.models import Proyec
from apps.sprint.models import HistoriaUsuario, Sprint, Actividad, Historial_HU, Estado_HU
from apps.user.models import User
from apps.proyectos.forms import ProyectoForm,rechazar_usform,configurarUSform, aprobar_usform, CrearUSForm, estimar_userform, editarProyect

class ProyectModelTest(TestCase):
    '''test del modelo Proyec'''
    @classmethod
    def setUpTestData(cls):
        '''se establecen los datos del modelo Proyect para las pruebas'''
        user=User.objects.create(first_name='Jose', last_name='Garcete', username='jose7', email="afasdfasd@gmail.com")
        Proyec.objects.create(nombre='tienda', descripcion='hola que tal', encargado=user)
#se compueba los campos de la clase.
    def test_name_label(self):
        '''test del label del atributo nombre del modelo Proyect'''
        project = Proyec.objects.get(nombre='tienda')
        field_label = project._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')
    def test_estado(self):
        '''test del label del atributo estado del modelo Proyect'''
        project = Proyec.objects.get(nombre='tienda')
        field_label = project._meta.get_field('estado').verbose_name
        self.assertEquals(field_label, 'estado')
#necesitamos probar nuestros métodos personalizados, el siguiente solo verifica que el nombre del objeto se construyó como esperábamos usando el formato "nombre"
    def test_descripcion(self):
        '''test del label del  atributo descripcion de la clase Proyect'''
        project = Proyec.objects.get(nombre='tienda')
        field_label = project._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label, 'descripcion')
    def test_encargado(self):
        '''test del label del atributo encargado del modelo Proyect'''
        project = Proyec.objects.get(nombre='tienda')
        field_label = project._meta.get_field('encargado').verbose_name
        self.assertEquals(field_label, 'encargado')
    def test_fecha_creacion(self):
        '''test del label del atributo fecha_creacion del modelo Proyect'''
        project = Proyec.objects.get(nombre='tienda')
        field_label = project._meta.get_field('fecha_creacion').verbose_name
        self.assertEquals(field_label, 'fecha de creacion')

    def test_fecha(self):
        '''test del label del atributo fecha del modelo Proyect'''
        project = Proyec.objects.get(nombre='tienda')
        field_label = project._meta.get_field('fecha').verbose_name
        self.assertEquals(field_label, 'fecha')


    def test_object_nombre(self):
        '''test de la funcion str creada para el modelo Proyec '''
        project = Proyec.objects.get(nombre='tienda')
        expected_object_name = project.nombre
        self.assertEquals(expected_object_name, str(project))
# con ddf se generan objetos para luego comprobar la correcta creacion, tambien se comprueba la relacion ManytoMany entre los usuarios y el proyecto
    #se prueba el form de proyectos
    def test_forms_fail_ProyectoForm(self):
        '''test del formulario ProyectoForm detectando una Excepcion'''
        with pytest.raises(Exception):
            form_data = {'nombre': 'laadfdlf'}
            form = ProyectoForm(data=form_data)
            self.assertTrue(form.is_valid())

    def test_forms_editarProyect(self):
        '''test del formulario editarProyect'''
        with pytest.raises(Exception):
            form_data = {'nombre':'hola', 'descripcion':'akdasdja'}
            form = editarProyect(data=form_data)
            self.assertTrue(form.is_valid())
######################################################################################################################################################
fake = Faker()
class HistoriaUsuarioModelTest(TestCase):
    '''test del modelo Proyec'''
    @classmethod
    def setUpTestData(cls):
        '''establecemos datos para la prueba de los modelos HistoriaUsuario , Estado_HU, Historial_HU'''
        user = User.objects.create(first_name='Belen', last_name='Castillo', username='bl',
                                   email="afasdfasd@gmail.com")
        a1 = Actividad.objects.create(nombre='Actividad1', comentario='esta actividad1 para test')
        a2 = Actividad.objects.create(nombre='Actividad2', comentario='esta actividad2 para test')
        p=Proyec.objects.create(nombre='tienda1', descripcion='hola que tal', encargado=user)
        s=Sprint.objects.create(nombre='sprint1', proyecto=p)
        h=HistoriaUsuario.objects.create(nombre='vista inicio' , sprint=s, descripcion='agregar funcionalidad', asignacion=user, estado='ToDo', estimacion=0,
                                       prioridad='Media', proyecto=Proyec.objects.get(nombre='tienda1'),
                                       aprobado_PB=True, rechazado_PB=False, sprint_backlog=True, estimacion_scrum=5, estimacion_user=11, QA_aprobado=True)
        h.actividades.add(a1)
        h.actividades.add(a2)
        Estado_HU.objects.create(hu=h, sprint=s, estado='Pendiente')

    '''necesitamos probar nuestros métodos personalizados, 
        el siguiente solo verifica que el nombre
         del objeto se construyó como esperábamos usando el formato "nombre"'''
    def test_name(self):
        '''test del atributo nombre del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.nombre, 'vista inicio')
    def test_name_label(self):
        '''test del label del atributo nombre del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')
    def test_asignacion(self):
        '''test del label del atributo asignacion del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        user = User.objects.get(username='bl')
        self.assertEquals(Us.asignacion, user)
    def test_asignacion_label(self):
        '''test del label del atributo asignacion del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('asignacion').verbose_name
        self.assertEquals(field_label, 'asignacion')
    def test_descripcion(self):
        '''test del atributo descripcion del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.descripcion, 'agregar funcionalidad')
    def test_descripcion_label(self):
        '''test del label del atributo descripcion del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label, 'descripcion')

    def test_estado(self):
        '''test del atributo estado del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.estado, 'ToDo')

    def test_estado_label(self):
        '''test del label del atributo estado del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('estado').verbose_name
        self.assertEquals(field_label, 'estado')

    def test_estimacion_label(self):
        '''test del label del atributo estimacion del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('estimacion').verbose_name
        self.assertEquals(field_label, 'estimacion')

    def test_prioridad(self):
        '''test del atributo prioridad del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.prioridad, 'Media')

    def test_prioridad_label(self):
        '''test del label del atributo prioridad del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('prioridad').verbose_name
        self.assertEquals(field_label, 'prioridad')

    def test_prioridad_numerica(self):
        '''test del atributo prioridad_numerica del modelo Historia Usuario'''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.prioridad_numerica, 2)

    def test_fecha_creacion(self):
        '''test del label del atributo fecha_creacion del modelo Historia Usuario'''
        HU = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = HU._meta.get_field('fecha_creacion').verbose_name
        self.assertEquals(field_label, 'fecha cre')

    def test_fecha(self):
        '''test del label del atributo fecha del modelo Historia Usuario'''
        HU = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = HU._meta.get_field('fecha').verbose_name
        self.assertEquals(field_label, 'fecha')

    def test_object_nombre(self):
        '''Probamos nuestro funcion str del modelo Historia Usuario '''
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        expected_object_name = '%s' % (Us.nombre)
        self.assertEquals(expected_object_name, str(Us))

    def test_create_HU(self):
        '''con ddf se generan objetos para luego comprobar la correcta creacion, tambien se comprueba la relacion ManytoMany entre los usuarios y el proyecto'''
        Us = G(HistoriaUsuario)
        assert Us

    '''ponemos a prueba nuestros formularios '''
    @pytest.mark.django_db
    def test_forms_fail_CrearUSForm(self):
        '''se detecta una Exception de un formulario incompleto'''
        with pytest.raises(Exception):
            form_data = {'nombre': 'dkfaad'}
            form = CrearUSForm(data=form_data)
            self.assertTrue(form.is_valid())
    def test_forms_aprobar_us(self):
        '''Probamos la validez del form aprobar_us '''
        form_data = {'aprobado_PB': 'True'}
        form = aprobar_usform(data=form_data)
        self.assertTrue(form.is_valid())

    def test_forms_rechazar_usform(self):
        '''Probamos la validez del form rechazar_usform '''
        form_data = {'rechazado_PB': 'True'}
        form = rechazar_usform(data=form_data)
        self.assertTrue(form.is_valid())

    @pytest.mark.django_db
    def test_forms_fail_estimar_userform(self):
        '''se detecta una Exception de un formulario estimar_userform incorrecto'''
        with pytest.raises(Exception):
            form_data = {'estimacion_user': 'jajd'}
            form = estimar_userform(data=form_data)
            self.assertTrue(form.is_valid())
    @pytest.mark.django_db
    def test_forms_fail2_estimar_userform(self):
        '''se detecta una Exception de un formulario estimar_userform incorrecto'''
        with pytest.raises(Exception):
            form_data = {'estimacion_user': -10}
            form = estimar_userform(data=form_data)
            self.assertTrue(form.is_valid())

    def test_forms_CrearUSForm(self):
        '''Probamos la validez del form CrearUSForm '''
        form_data = {'nombre': 'afadf', 'descripcion':'asdkfjasadds', 'prioridad':'Media'}
        form = CrearUSForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_forms_CrearUSForm_fail(self):
        '''se detecta una Exception de un formulario CrearUSForm incorrecto'''
        with pytest.raises(Exception):
            form_data = {'nombre': 'afadf', 'descripcion':'asdkfjasadds', 'prioridad':'hola'}
            form = CrearUSForm(data=form_data)
            self.assertTrue(form.is_valid())
    def test_forms_CrearUSForm_fail2(self):
        '''se detecta una Exception de un formulario CrearUSForm incorrecto'''
        with pytest.raises(Exception):
            form_data = {'nombre': 'afadf'}
            form = CrearUSForm(data=form_data)
            self.assertTrue(form.is_valid())
    def test_forms_estimar_userform(self):
        '''Probamos la validez del form estimar_userform '''
        form_data = {'estimacion_user': 10}
        form = estimar_userform(data=form_data)
        self.assertTrue(form.is_valid())

    @pytest.mark.django_db
    def test_forms_configurarUSform(self):
        '''se detecta una Exception de un formulario configurarUSform incorrecto'''
        with pytest.raises(Exception):
            form_data = {'estimacion_scrum': 10}
            form = configurarUSform(data=form_data)
            self.assertTrue(form.is_valid())




    def test_estimacion_user(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.estimacion_user, 11)
    def test_estimacion_scrum(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.estimacion_scrum, 5)
    def test_def_planing_poker(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.estimacion, 8)
    def test_estimacion_scrum(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.estimacion_scrum, 5)

    def test_aprobado_PB(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.aprobado_PB, True)


    def test_rechazado_PB(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.rechazado_PB, False)


    def test_proyectoHU(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        proyecto=Proyec.objects.get(nombre='tienda1')
        self.assertEquals(Us.proyecto, proyecto)
        self.assertEquals(Us.proyecto_id, proyecto.id)
    def test_proyecto_label(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('proyecto').verbose_name
        self.assertEquals(field_label, 'proyecto')
    def test_sprintHU(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        sprint=Sprint.objects.get(nombre='sprint1')
        self.assertEquals(Us.sprint, sprint)
        self.assertEquals(Us.sprint_id, sprint.id)
    def test_sprint_label(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('sprint').verbose_name
        self.assertEquals(field_label, 'sprint')
    def test_actividad_HU(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        ac=Actividad.objects.get(nombre='Actividad1')
        self.assertEquals(Us.actividades.first(), ac)
    def test_actividad_count_HU(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(Us.actividades.count(), 2)
    def test_actividad_label(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        field_label = Us._meta.get_field('actividades').verbose_name
        self.assertEquals(field_label, 'actividades')




    ############################################HistorialHU############################################################
    def test_descripcion_historial(self):
        historial=Historial_HU.objects.get(id=1)
        self.assertEquals(historial.descripcion, ' Resultado del Planning Poker: 8.0')
    def test_descripcion_historial_label(self):
        historial=Historial_HU.objects.get(id=1)
        field_label = historial._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label, 'descripcion')

    def test_fecha_creacion_label(self):
        historial=Historial_HU.objects.get(id=1)
        field_label = historial._meta.get_field('fecha_creacion').verbose_name
        self.assertEquals(field_label, 'fecha cre')

    def test_hora_label(self):
        historial=Historial_HU.objects.get(id=1)
        field_label = historial._meta.get_field('hora').verbose_name
        self.assertEquals(field_label, 'hora')
    def test_hu_label(self):
        historial=Historial_HU.objects.get(id=1)
        field_label = historial._meta.get_field('hu').verbose_name
        self.assertEquals(field_label, 'hu')
    def test_hu_historial(self):
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        historial=Historial_HU.objects.get(id=1)
        self.assertEquals(historial.hu, Us)

#########################################################################Estado_HU#################################
    def test_hu_Estado_hu_label(self):
        e = Estado_HU.objects.get(id=1)
        field_label = e._meta.get_field('hu').verbose_name
        self.assertEquals(field_label, 'hu')
    def test_hu_Estado_hu(self):
        e = Estado_HU.objects.get(id=1)
        Us = HistoriaUsuario.objects.get(nombre='vista inicio')
        self.assertEquals(e.hu, Us)


    def test_sprint_Estado_hu_label(self):
        e = Estado_HU.objects.get(id=1)
        field_label = e._meta.get_field('sprint').verbose_name
        self.assertEquals(field_label, 'sprint')

    def test_sprint_Estado_hu(self):
        e = Estado_HU.objects.get(id=1)
        sprint = Sprint.objects.get(nombre='sprint1')
        self.assertEquals(e.sprint, sprint)

    def test_estado_Estado_hu_label(self):
        e = Estado_HU.objects.get(id=1)
        field_label = e._meta.get_field('estado').verbose_name
        self.assertEquals(field_label, 'estado')

    def test_estado_Estado_hu(self):
        e = Estado_HU.objects.get(id=1)
        self.assertEquals(e.estado, 'Pendiente')

    def test_prioridad_Estado_hu(self):
        e = Estado_HU.objects.get(id=1)
        self.assertEquals(e.prioridad, 'Baja')
    def test_prioridad_Estado_hu_label(self):
        e = Estado_HU.objects.get(id=1)
        field_label = e._meta.get_field('prioridad').verbose_name
        self.assertEquals(field_label, 'prioridad')
    def test_desarrollador_Estado_hu_label(self):
        e = Estado_HU.objects.get(id=1)
        field_label = e._meta.get_field('desarrollador').verbose_name
        self.assertEquals(field_label, 'desarrollador')

    def test_desarrollador_Estado_hu(self):
        e = Estado_HU.objects.get(id=1)
        self.assertEquals(e.desarrollador, 'User')
    def test_PP_Estado_hu(self):
        e = Estado_HU.objects.get(id=1)
        self.assertEquals(e.PP, 0)

class SprintModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(first_name='Belen', last_name='Lopez', username='belen',
                                   email="afasdfasd@gmail.com")
        user2 = User.objects.create(first_name='Rosana', last_name='Lopez', username='ross',
                                    email="afasdfasd@gmail.com")
        p = Proyec.objects.create(nombre='is2', descripcion='hola que tal', encargado=user1)
        s = Sprint.objects.create(nombre='sprint2', proyecto=p, estado="Pendiente")
        s.equipo.add(user1)
        s.equipo.add(user2)
    def test_name(self):
        s = Sprint.objects.get(nombre='sprint2')
        self.assertEquals(s.nombre, 'sprint2')

    def test_name_label(self):
        s = Sprint.objects.get(nombre='sprint2')
        field_label = s._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_object_nombre(self):
        '''test de la funcion str creada para el modelo Sprint '''
        s = Sprint.objects.get(nombre='sprint2')
        expected_object_name = s.nombre
        self.assertEquals(expected_object_name, str(s))

    def test_proyecto_label(self):
        s = Sprint.objects.get(nombre='sprint2')
        field_label = s._meta.get_field('proyecto').verbose_name
        self.assertEquals(field_label, 'proyecto')
    def test_proyecto(self):
        s = Sprint.objects.get(nombre='sprint2')
        p = Proyec.objects.get(nombre='is2')
        self.assertEquals(s.proyecto, p)
    def test_fecha_inicio_label(self):
        s = Sprint.objects.get(nombre='sprint2')
        field_label = s._meta.get_field('fecha_inicio').verbose_name
        self.assertEquals(field_label, 'fecha inicio')
    def test_fecha_fin_label(self):
        s = Sprint.objects.get(nombre='sprint2')
        field_label = s._meta.get_field('fecha_fin').verbose_name
        self.assertEquals(field_label, 'fecha fin')

    def test_fecha_creacion_label(self):
        s = Sprint.objects.get(nombre='sprint2')
        field_label = s._meta.get_field('fecha_creacion').verbose_name
        self.assertEquals(field_label, 'fecha de creacion')

    def test_equipo_label(self):
        s = Sprint.objects.get(nombre='sprint2')
        field_label = s._meta.get_field('equipo').verbose_name
        self.assertEquals(field_label, 'equipo')

    def test_equipo_count(self):
        s = Sprint.objects.get(nombre='sprint2')
        self.assertEquals(s.equipo.count(), 2)
    def test_equipo_sprint(self):
        s = Sprint.objects.get(nombre='sprint2')
        user=User.objects.get(username='belen')
        self.assertEquals(s.equipo.first(), user)
    def test_capacidad_equipo_label(self):
        s = Sprint.objects.get(nombre='sprint2')
        field_label = s._meta.get_field('capacidad_equipo').verbose_name
        self.assertEquals(field_label, 'capacidad equipo')
    def test_capacidad_equipo(self):
        s = Sprint.objects.get(nombre='sprint2')
        self.assertEquals(s.capacidad_equipo, 0)

    def test_capacidad_de_equipo_sprint(self):
        s = Sprint.objects.get(nombre='sprint2')
        self.assertEquals(s.capacidad_de_equipo_sprint, 0)



class ActividadModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Actividad.objects.create(nombre='actividadprueba',
                                 hora_trabajo=11, comentario='esto es una prueba',
                                 id_sprint=2)
    def test_name(self):
        a = Actividad.objects.get(nombre='actividadprueba')
        self.assertEquals(a.nombre, 'actividadprueba')

    def test_name_label(self):
        a = Actividad.objects.get(nombre='actividadprueba')
        field_label = a._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_object_nombre(self):
        '''test de la funcion str creada para el modelo Sprint '''
        a = Actividad.objects.get(nombre='actividadprueba')
        expected_object_name = a.nombre
        self.assertEquals(expected_object_name, str(a))

    def test_comentario(self):
        a = Actividad.objects.get(nombre='actividadprueba')
        self.assertEquals(a.comentario, 'esto es una prueba')

    def test_comentario_label(self):
        a = Actividad.objects.get(nombre='actividadprueba')
        field_label = a._meta.get_field('comentario').verbose_name
        self.assertEquals(field_label, 'comentario')
    def test_fecha_label(self):
        a = Actividad.objects.get(nombre='actividadprueba')
        field_label = a._meta.get_field('fecha').verbose_name
        self.assertEquals(field_label, 'fecha')
    def test_hora_trabajo(self):
        a = Actividad.objects.get(nombre='actividadprueba')
        self.assertEquals(a.hora_trabajo, 11)

    def test_id_sprint(self):
        a = Actividad.objects.get(nombre='actividadprueba')
        self.assertEquals(a.id_sprint, 2)




