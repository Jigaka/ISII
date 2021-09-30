from django.db import models
from django.db.models.signals import post_save, pre_save
from apps.proyectos.models import Proyec, HistoriaUsuario
# Create your models here.
class Sprint(models.Model):
    Pendiente = 'Pendiente'
    Iniciado = 'Iniciado'
    Finalizado = 'Finalizado'
    STATUS_CHOICES = (
        (Pendiente, "Pendiente"),
        (Iniciado, "Iniciado"),
        (Finalizado, "Finalizado")
    )
    nombre = models.CharField(max_length=200, blank=False, null=False)
    proyecto = models.ForeignKey(Proyec, blank=False, null=False, on_delete=models.CASCADE, related_name="proyecto_s")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=15, choices=STATUS_CHOICES, default=1)  # pendiente,iniciado,finalizado
    hu = models.ManyToManyField(HistoriaUsuario,blank=True, null=True, related_name="hu", limit_choices_to={'aprobado_PB':True, 'sprint_backlog':False})

    # capacidad_de_equipo (sumar la capacidad diaria de cada integrnte y multiplicarlo por la cantidad de días), , limit_choices_to={'aprobado_PB':True, 'sprint_backlog':False}

    # La cantidad de días incluye fines de semana (¿cómo resolver esto?)
    @property
    def duracion_dias(self):
        if (self.fecha_inicio and self.fecha_fin):
            duracion_dias = self.fecha_fin - self.fecha_inicio
            return duracion_dias

    class Meta:
        verbose_name = 'Sprint'
        verbose_name_plural = 'Sprints'

    def __str__(self):
        return self.nombre
'''
def modificarHU(sender, instance, **kwargs):
   # for x in instance:
   #Sprint.objects.get(id=instance.id).hu.all().update( aprobado_PB=False)
   Sprint.objects.get(id=instance.id).hu.all().update(sprint_backlog=True)

post_save.connect(modificarHU, sender=Sprint)
'''