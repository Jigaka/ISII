import pytest
from django.test import TestCase
from faker import Faker
from ddf import G, F
from apps.proyectos.models import Proyec
from apps.sprint.models import HistoriaUsuario, Sprint
from apps.user.models import User
from apps.proyectos.forms import ProyectoForm,configurarUSform, aprobar_usform, CrearUSForm, estimar_userform, editarProyect

class ProyectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user=User.objects.create(first_name='Jose', last_name='Garcete', username='jose7', email="afasdfasd@gmail.com")
        Proyec.objects.create(nombre='tienda', descripcion='hola que tal', encargado=user)
#se compueba los campos de la clase.
    def test_name_label(self):
        project = Proyec.objects.get(id=2)
        field_label = project._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')
    def test_estado(self):
        project = Proyec.objects.get(id=2)
        field_label = project._meta.get_field('estado').verbose_name
        self.assertEquals(field_label, 'estado')
#necesitamos probar nuestros métodos personalizados, el siguiente solo verifica que el nombre del objeto se construyó como esperábamos usando el formato "nombre"
    def test_descripcion(self):
        project = Proyec.objects.get(id=2)
        field_label = project._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label, 'descripcion')
    def test_encargado(self):
        project = Proyec.objects.get(id=2)
        field_label = project._meta.get_field('encargado').verbose_name
        self.assertEquals(field_label, 'encargado')
    def test_fecha_creacion(self):
        project = Proyec.objects.get(id=2)
        field_label = project._meta.get_field('fecha_creacion').verbose_name
        self.assertEquals(field_label, 'fecha de creacion')

    def test_fecha(self):
        project = Proyec.objects.get(id=2)
        field_label = project._meta.get_field('fecha').verbose_name
        self.assertEquals(field_label, 'fecha')

    def test_descripcion(self):
        project = Proyec.objects.get(id=2)
        field_label = project._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label, 'descripcion')
    def test_object_nombre(self):
        project = Proyec.objects.get(id=2)
        expected_object_name = project.nombre
        self.assertEquals(expected_object_name, str(project))
# con ddf se generan objetos para luego comprobar la correcta creacion, tambien se comprueba la relacion ManytoMany entre los usuarios y el proyecto
    #se prueba el form de proyectos
    def test_forms_fail_ProyectoForm(self):
        with pytest.raises(Exception):
            form_data = {'nombre': 'laadfdlf'}
            form = ProyectoForm(data=form_data)
            self.assertTrue(form.is_valid())

    def test_forms_editarProyect(self):
        with pytest.raises(Exception):
            form_data = {'nombre':'hola', 'descripcion':'akdasdja'}
            form = editarProyect(data=form_data)
            self.assertTrue(form.is_valid())
######################################################################################################################################################
fake = Faker()
class HistoriaUsuarioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #proyecto=Proyec.objects.get(id=1)
        user = User.objects.create(first_name='Belen', last_name='Castillo', username='bl',
                                   email="afasdfasd@gmail.com")
        #sprint=Sprint.objects.create(nombre='sprint1', proyecto=proyecto)
        HistoriaUsuario.objects.create(nombre='vista inicio', descripcion='agregar funcionalidad', asignacion=user, estado='ToDo', estimacion=0, prioridad='Media')
#se compueba los campos de la clase.
    def test_name(self):
        Us = HistoriaUsuario.objects.get(id=1)
        self.assertEquals(Us.nombre, 'vista inicio')

    def test_asignacion(self):
        Us = HistoriaUsuario.objects.get(id=1)
        user = User.objects.get(username='bl')
        self.assertEquals(Us.asignacion, user)

    '''def test_sprint(self):
        sprint = Sprint.objects.get(id=1)
        Us = HistoriaUsuario.objects.get(id=1)
        self.assertEquals(Us.sprint, sprint)'''
    def test_descripcion(self):
        Us = HistoriaUsuario.objects.get(id=1)
        self.assertEquals(Us.descripcion, 'agregar funcionalidad')
    def test_estado(self):
        Us = HistoriaUsuario.objects.get(id=1)
        self.assertEquals(Us.estado, 'ToDo')
    def test_estimacion(self):
        Us = HistoriaUsuario.objects.get(id=1)
        self.assertEquals(Us.estimacion, 0)
    def test_prioridad(self):
        Us = HistoriaUsuario.objects.get(id=1)
        self.assertEquals(Us.prioridad, 'Media')

    def test_prioridad_numerica(self):
        Us = HistoriaUsuario.objects.get(id=1)
        self.assertEquals(Us.prioridad_numerica, 2)

#necesitamos probar nuestros métodos personalizados, el siguiente solo verifica que el nombre del objeto se construyó como esperábamos usando el formato "nombre"
    def test_fecha_creacion(self):
        HU = HistoriaUsuario.objects.get(id=1)
        field_label = HU._meta.get_field('fecha_creacion').verbose_name
        self.assertEquals(field_label, 'fecha cre')

    def test_fecha(self):
        HU = HistoriaUsuario.objects.get(id=1)
        field_label = HU._meta.get_field('fecha').verbose_name
        self.assertEquals(field_label, 'fecha')

    def test_object_nombre(self):
        Us = HistoriaUsuario.objects.get(id=1)
        expected_object_name = '%s' % (Us.nombre)
        self.assertEquals(expected_object_name, str(Us))
# con ddf se generan objetos para luego comprobar la correcta creacion, tambien se comprueba la relacion ManytoMany entre los usuarios y el proyecto
    def test_create_HU(self):
        Us = G(HistoriaUsuario)
        assert Us
    @pytest.mark.django_db
    #se prueba el form de proyectos
    def test_forms_fail_CrearUSForm(self):
        with pytest.raises(Exception):
            form_data = {'nombre': 'dkfaad'}
            form = CrearUSForm(data=form_data)
            self.assertTrue(form.is_valid())


    def test_forms_aprobar_us(self):
        form_data = {'aprobado_PB': 'True'}
        form = aprobar_usform(data=form_data)
        self.assertTrue(form.is_valid())



    @pytest.mark.django_db
    def test_forms_fail_estimar_userform(self):
        with pytest.raises(Exception):
            form_data = {'estimacion_user': 'jajd'}
            form = estimar_userform(data=form_data)
            self.assertTrue(form.is_valid())

    @pytest.mark.django_db
    def test_forms_fail2_estimar_userform(self):
        with pytest.raises(Exception):
            form_data = {'estimacion_user': -10}
            form = estimar_userform(data=form_data)
            self.assertTrue(form.is_valid())

    def test_forms_CrearUSForm(self):
        form_data = {'nombre': 'afadf', 'descripcion':'asdkfjasadds', 'prioridad':'Media'}
        form = CrearUSForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_forms_CrearUSForm_fail(self):
        with pytest.raises(Exception):
            form_data = {'nombre': 'afadf', 'descripcion':'asdkfjasadds', 'prioridad':'Jose'}
            form = CrearUSForm(data=form_data)
            self.assertTrue(form.is_valid())
    def test_forms_CrearUSForm_fail2(self):
        with pytest.raises(Exception):
            form_data = {'nombre': 'afadf'}
            form = CrearUSForm(data=form_data)
            self.assertTrue(form.is_valid())
    def test_forms_estimar_userform(self):
        form_data = {'estimacion_user': 10}
        form = estimar_userform(data=form_data)
        self.assertTrue(form.is_valid())

    @pytest.mark.django_db
    def test_forms_configurarUSform(self):
        with pytest.raises(Exception):
            form_data = {'estimacion_scrum': 10}
            form = configurarUSform(data=form_data)
            self.assertTrue(form.is_valid())