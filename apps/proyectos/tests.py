
import pytest
from django.test import TestCase
from faker import Faker
from ddf import G, F
from apps.user.models import User
from apps.proyectos.models import Proyec
from apps.proyectos.forms import ProyectoForm

fake = Faker()
class ProyectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Proyec.objects.create(nombre='tienda ')
#se compueba los campos de la clase.
    def test_first_name_label(self):
        proyecto = Proyec.objects.get(id=1)
        field_label = proyecto._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')
    def test_estado(self):
        proyecto = Proyec.objects.get(id=1)
        field_label = proyecto._meta.get_field('estado').verbose_name
        self.assertEquals(field_label, 'estado')
#necesitamos probar nuestros métodos personalizados, el siguiente solo verifica que el nombre del objeto se construyó como esperábamos usando el formato "nombre"
    def test_object_nombre(self):
        proyecto = Proyec.objects.get(id=1)
        expected_object_name = '%s' % (proyecto.nombre)
        self.assertEquals(expected_object_name, str(proyecto))
# con ddf se generan objetos para luego comprobar la correcta creacion, tambien se comprueba la relacion ManytoMany entre los usuarios y el proyecto
    def test_create_Proyec(self):
        proyecto1 = G(Proyec)
        assert proyecto1
    @pytest.mark.django_db
    #se prueba el form de proyectos
    def test_forms_fail(self):
        with pytest.raises(Exception):
            form_data = {'nombre': 'laadfdlf'}
            form = ProyectoForm(data=form_data)
            self.assertTrue(form.is_valid())






