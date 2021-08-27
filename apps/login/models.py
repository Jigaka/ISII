from django.db import models

class ListaPermitidos(models.Model):
    correo = models.TextField()

    def __str__(self):
        return f'{self.correo}'