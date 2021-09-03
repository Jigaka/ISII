from django.test import TestCase, Client
import pytest

# Create your tests here.
#se prueba que un cliente, sin registrarse no ingrese
class loginTestCase(TestCase):
    def test_index(self):
        # Crear un cliente
        client = Client()
        # Simule al cliente que visite la página de inicio
        response = client.get('/')
        # Probar el código de estado devuelto desde la página de inicio
        with pytest.raises(Exception):
            self.assertEqual(
                response.status_code,
                200,
                'El código de estado del índice no es 200'
            )