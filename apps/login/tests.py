import pytest
from django.test import TestCase, Client

import json

from rest_framework.reverse import reverse

from apps.user.models import User
from django.test import TestCase
from apps.proyectos.models import Proyec
from rest_framework.test import APITestCase, force_authenticate


class noLoginTestCase(APITestCase):
    def setUp(self):
        self.username = 'john_doe'
        self.password = 'foobar'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        #self.client.force_login(user=self.user)

    def test_1(self):
        '''se comprueba  /login/'''
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)


    def test_2(self):
        '''se comprueba que no le de acceso al inicio a un usuario sin hacer login y que se redirija a login'''
        response = self.client.get('/inicio/')
        self.assertEqual(response.status_code, 302)


    def test_3(self):
        '''se comprueba que al no tener acceso al inicio se redirija a login'''
        response = self.client.get('/')
        redir=response['location']
        self.assertEqual(redir, 'login')
    '''def test_4(self):
        response = self.client.get(reverse('check_user'))
        self.assertEqual(response.status_code, 200)'''

    def test_sin_login_proyectos(self):
        '''se comprueba que no le de acceso al inicio a un usuario sin hacer login y que se redirija a login'''
        response = self.client.get('/proyectos/listar_proyectos/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/crear_proyecto/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/listar_proyectos/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/editar_proyecto/1')
        self.assertEqual(response.status_code, 301)
        response = self.client.get('/proyectos/eliminar_proyecto/1')
        self.assertEqual(response.status_code, 301)
        response = self.client.get('/proyectos/listar_integrantes/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/ver_proyecto/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/mis_proyectos/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/ver_proyecto/1')
        self.assertEqual(response.status_code, 302)



    def test_sin_login_HU(self):
        '''se comprueba que no le de acceso al inicio a un usuario sin hacer login y que se redirija a login'''
        #user = User.objects.create(first_name='Jose', last_name='Garcete', username='jose7',
        #                           email="afasdfasd@gmail.com")
        #Proyec.objects.create(nombre='tienda', descripcion='hola que tal', encargado=user)
        response = self.client.get('/proyectos/listar_us/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/crear_us/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/editar_us/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/eliminar_us/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/aprobar_us/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/listar_us_a_estimar_us/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/estimar_us/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/proyectos/ver_PB/1')
        self.assertEqual(response.status_code, 302)



    def test_sin_login_sprint(self):
        '''se comprueba que no le de acceso al inicio a un usuario sin hacer login y que se redirija a login'''
        user = User.objects.create(first_name='Jose', last_name='Garcete', username='jose7',
                                   email="afasdfasd@gmail.com")
        Proyec.objects.create(nombre='tienda', descripcion='hola que tal', encargado=user)

        response = self.client.get('/sprint/crear_sprint/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/listar_sprint/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/agregar_hu/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/ver_sprint/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/ver_sb/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/configurar_equipo/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/configurar_us/1')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/sprint/cambio_estadoHU/1')
        self.assertEqual(response.status_code, 302)


    '''def test_con_login_proyectos(self):
        self.client.force_login(user=self.user)
        #self.client.login()
        response = self.client.get('/proyectos/listar_proyectos/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/proyectos/crear_proyecto/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/proyectos/listar_proyectos/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/proyectos/editar_proyecto/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/proyectos/eliminar_proyecto/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/proyectos/listar_integrantes/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/proyectos/ver_proyecto/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/proyectos/mis_proyectos/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/proyectos/ver_proyecto/1')
        self.assertEqual(response.status_code, 200)'''