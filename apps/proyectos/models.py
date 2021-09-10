from django.db import models
from apps.user.models import User, Rol


'''
Modelo para el proyecto a desarrollar.
Este represe la clase del proyecto, el cual contiene
los estados, el nombre, descripcion y los miembros.
'''
class Proyec(models.Model):
    Pendiente='Pendiente'
    Iniciado='Iniciado'
    Concluido='Concluido'
    Cancelado='Cancelado'
    STATUS_CHOICES = (
        (Pendiente, "Pendiente"),
        (Iniciado, "Iniciado"),
        (Concluido, "Concluido"),
        (Cancelado, "Cancelado")
    )
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200,blank=False, null= False )
    equipo= models.ManyToManyField(User, related_name="equipo")
    descripcion=models.TextField(blank=False, null=False)
    estado=models.CharField(max_length=15 , choices=STATUS_CHOICES, default=1 )
    fecha = models.DateField("fecha", auto_now=True, auto_now_add=False)
    #fecha_inicio=models.DateField()
    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural = 'Proyectos'
    def __str__(self):
        return self.nombre

    def is_upperclass(self):
        return self.estado in {self.Pendiente, self.Iniciado, self.Cancelado , self.Concluido}


class RolProyecto(models.Model):
    '''
    Modelo para relacionar un rol con un proyecto.
    Un proyecto puede tener varios roles, ademas esto permitira
    importar roles desde un proyecto a otro.
    '''
    nombre = models.CharField(max_length=50, blank=False, null=False)
    proyecto = models.ForeignKey(Proyec, on_delete=models.CASCADE, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name='RolProyecto'
        verbose_name_plural = 'RolesProyectos'

    def __str__(self):
        return self.nombre
