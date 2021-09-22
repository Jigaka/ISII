from django.test import TestCase
import pytest
import factory
from faker import Faker
from django.test import TestCase, Client
from apps.user.models import User, Rol
from apps.user.forms import UserForm
from ddf import G, F


class UserTestCase(TestCase):
    #con ddf se prueba si en verdad se crea un objeto user
    def test_create_User(self):
        usuario=G(User)
        assert usuario
    # se pueba los campos de la clase.
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(first_name='Jose', last_name='Garcete', username='big8', email="afasdfasd@gmail.com")

    def test_first_name_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_email_label(self):
        usuario= User.objects.get(id=1)
        field_label = usuario._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'dirección de correo electrónico')

    #@pytest.mark.django_db


###############################################################################################################################################
class RolTestCase(TestCase):
    #con ddf se prueba si en verdad se crea un objeto rol
    def test_create_rol(self):
        rol=G(Rol)
        assert rol
