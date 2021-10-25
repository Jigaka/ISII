from sqlite3 import Date

from django.db import models
from django.db.models.signals import post_save, pre_save
from apps.proyectos.models import Proyec
from apps.user.models import User
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
    estado = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pendiente')  # pendiente,iniciado,finalizado
    equipo = models.ManyToManyField(User, related_name="equipo_s")
    fecha_creacion = models.DateField("fecha de creacion", auto_now=False, auto_now_add=True, blank=True, null=True)
    capacidad_equipo = models.PositiveIntegerField(editable=True, default=0)
    capacidad_de_equipo_sprint = models.PositiveIntegerField(editable=True, default=0)

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
class HistoriaUsuario(models.Model):
    Pendiente = 'Pendiente'
    ToDo = 'ToDo'
    Doing = 'Doing'
    Done = 'Done'
    QA = 'QA'
    STATUS_CHOICES = (
        (Pendiente, "Pendiente"),
        (ToDo, 'ToDo'),
        (Doing, 'Doing'),
        (Done, 'Done'),
        (QA, 'QA')
    )

    Baja = 'Baja'
    Media = 'Media'
    Alta = 'Alta'
    Prioridad_CHOICES = (
        (Baja, 'Baja'),
        (Media, 'Media'),
        (Alta, 'Alta'),
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False, unique=True)
    asignacion = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True, related_name="asignacion")
    product_owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="PO")
    descripcion = models.TextField(blank=False, null=False)
    estado = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pendiente')
    fecha = models.DateField("fecha", auto_now=True, auto_now_add=False)
    estimacion = models.PositiveIntegerField(editable=True, default=0)
    fecha_creacion = models.DateField("fecha cre", auto_now=False, auto_now_add=True, blank=True, null=True)
    fecha_ToDo = models.DateField(blank=True, null=True, )
    fecha_Doing = models.DateField(blank=True, null=True)
    fecha_Done = models.DateField(blank=True, null=True)
    fecha_QA = models.DateField(blank=True, null=True)
    estado_anterior = models.CharField(max_length=200, default='Pendiente')
    prioridad = models.CharField(max_length=15, choices=Prioridad_CHOICES, default=1)
    prioridad_numerica = models.IntegerField(null=False, default=1)
    proyecto = models.ForeignKey(Proyec, on_delete=models.CASCADE, blank=True, null=True, related_name="proyecto")
    aprobado_PB = models.BooleanField(default=False)
    rechazado_PB = models.BooleanField(default=False)
    sprint_backlog = models.BooleanField(default=False)
    estimacion_user = models.PositiveIntegerField(editable=True, default=0)
    estimacion_scrum = models.PositiveIntegerField(editable=True, default=0)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True, related_name="sprint", limit_choices_to={'estado': 'Pendiente'})
    QA_aprobado=models.BooleanField(default=False)
    def save(self, *args, **kwargs):  # redefinicion del metodo save() que contiene nuestro trigger limit_choices_to={'aprobado_PB': True, 'sprint_backlog': False}
        # Aqui ponemos el codigo del trigger -------
        if (self.prioridad == 'Baja'):
            self.prioridad_numerica = 1
        elif (self.prioridad == 'Media'):
            self.prioridad_numerica = 2
        elif (self.prioridad == 'Alta'):
            self.prioridad_numerica = 3
        super(HistoriaUsuario, self).save(*args, **kwargs)
        # fin de trigger ------

    class Meta:
        verbose_name = 'Historia de Usuario'
        verbose_name_plural = 'Historias de Usuario'

    def __str__(self):
        return self.nombre

    def is_upperclass(self):
        return self.prioridad in {self.Baja, self.Media, self.Alta}

    def is_upperclasss(self):
        return self.estado in {self.Pendiente, self.ToDo, self.Doing, self.Done, self.QA}

    def obtener_asignacion(self):
        asignacion_user = self.asignacion.all().values_list('username', flat=True)
        return asignacion_user


def calcular_estimacion(sender, instance, **kwargs):
    if (instance.estimacion==0 and  instance.estimacion_scrum!=0 and instance.estimacion_user!=0):
        x=(instance.estimacion_scrum+instance.estimacion_user)/2
        HistoriaUsuario.objects.filter(id=instance.id).update(estimacion=x)
        Historial_HU.objects.create(
            descripcion=' Resultado del Planning Poker: ' + x.__str__(), hu=HistoriaUsuario.objects.get(id=instance.id))
post_save.connect(calcular_estimacion, sender=HistoriaUsuario)
class CapacidadDiariaEnSprint(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name="el_usuario")
    sprint= models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=False, null=False, related_name="el_sprint")
    capacidad_diaria_horas=models.PositiveIntegerField(null=False, default=8)
    models.UniqueConstraint(fields = ['usuario', 'sprint'], name = 'restriccion_par_usuario_sprint')

def capacidad_equipo_por_sprint(sender, instance, **kwargs):
    #Se calcula la suma de todas las horas de trabajo de los desarrolladores
    sprint = instance.sprint
    print("MODELSS", sprint.id)
    capacidad_diaria = instance.capacidad_diaria_horas
    print(Sprint.objects.filter(id=sprint.id).first().capacidad_equipo)
    capacidad_suma = Sprint.objects.filter(id=sprint.id).first().capacidad_equipo + capacidad_diaria
    Sprint.objects.filter(id=sprint.id).update(capacidad_equipo=capacidad_suma)
    print("ESTOY EN MODELS ",capacidad_suma)
    duracion_dias = sprint.fecha_fin - sprint.fecha_inicio
    dias = duracion_dias.days
    calculo_de_la_capacidad = duracion_dias.days*capacidad_suma
    print("Duracion ",duracion_dias)
    print("calculo ",calculo_de_la_capacidad)
    Sprint.objects.filter(id=sprint.id).update(capacidad_de_equipo_sprint=calculo_de_la_capacidad)
post_save.connect(capacidad_equipo_por_sprint, sender=CapacidadDiariaEnSprint)
class Historial_HU(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField("fecha cre", auto_now=False, auto_now_add=True, blank=True, null=True)
    descripcion = models.TextField(blank=False, null=False)
    hora = models.TimeField(auto_now_add=True, blank=True, null=True)
    hu = models.ForeignKey(HistoriaUsuario, on_delete=models.CASCADE, blank=True, null=True, related_name="historial_hu")

class Estado_HU(models.Model):
    id = models.AutoField(primary_key=True)
    hu = models.ForeignKey(HistoriaUsuario, on_delete=models.CASCADE, blank=True, null=True,related_name="estado_hu")
    sprint=models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True,related_name="estado_sprint")
    estado = models.TextField(blank=False, null=False)
    prioridad = models.TextField(blank=False, null=False, default='Baja')
    desarrollador = models.TextField(blank=False, null=False, default='User')
    PP= models.IntegerField(blank=False, null=False, default=0)