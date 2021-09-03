from django.db import models

'''
Modelo para controlar el acceso al sistema
de personas no autorizadas. Atraves del atributo 
correo
'''
class ListaPermitidos(models.Model):
    correo = models.TextField()

    def __str__(self):
        return f'{self.correo}'