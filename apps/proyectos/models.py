from django.db import models
from django.contrib.auth.models import Permission, Group
from django.db.models.signals import post_save, pre_save
from apps.user.models import User, Rol




'''
Modelo para el proyecto a desarrollar.
Este represe la clase del proyecto, el cual contiene
los estados, el nombre, descripcion y los miembros.
'''
class Proyec(models.Model):
    Pendiente = 'Pendiente'
    Iniciado = 'Iniciado'
    Concluido = 'Concluido'
    Cancelado = 'Cancelado'
    STATUS_CHOICES = (
        (Pendiente, "Pendiente"),
        (Iniciado, "Iniciado"),
        (Concluido, "Concluido"),
        (Cancelado, "Cancelado")
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    # limit_choices_to={'rol':1}
    encargado = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="encargado")
    equipo = models.ManyToManyField(User, related_name="equipo")
    descripcion = models.TextField(blank=False, null=False)
    estado = models.CharField(max_length=15, choices=STATUS_CHOICES, default="Pendiente")
    fecha = models.DateField("fecha", auto_now=True, auto_now_add=False)
    dias_estimados = models.PositiveIntegerField(editable=True, default=0)
    fecha_creacion = models.DateField("fecha de creacion", auto_now=False, auto_now_add=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_concluido = models.DateField(blank=True, null=True)
    fecha_cancelado = models.DateField(blank=True, null=True)
    estado_anterior = models.CharField(max_length=200, default='Pendiente')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre

    def is_upperclass(self):
        return self.estado in {self.Pendiente, self.Iniciado, self.Cancelado, self.Concluido}

    def obtener_equipo(self):
        miembros = str([User for User in self.equipo.all().values_list('username', flat=True)]).replace("[",
                                                                                                        "").replace("]",
                                                                                                                    "").replace(
            "'", "")
        return miembros

    def obtener_encargado(self):
        encargado_del_proyecto = self.encargado.all().values_list('username', flat=True)
        return encargado_del_proyecto


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
    nombre = models.CharField(max_length=200, blank=False, null=False)
    asignacion = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True, related_name="asignacion")
    descripcion = models.TextField(blank=False, null=False)
    estado = models.CharField(max_length=15, choices=STATUS_CHOICES, default=1)
    fecha = models.DateField("fecha", auto_now=True, auto_now_add=False)
    estimacion = models.PositiveIntegerField(editable=True, default=0)
    fecha_creacion = models.DateField("fecha cre", auto_now=False, auto_now_add=True, blank=True, null=True)
    fecha_ToDo = models.DateField(blank=True, null=True)
    fecha_Doing = models.DateField(blank=True,null=True)
    fecha_Done = models.DateField(blank=True,null=True)
    fecha_QA = models.DateField(blank=True, null=True)
    estado_anterior = models.CharField(max_length=200, default='Pendiente')
    prioridad = models.CharField(max_length=15, choices=Prioridad_CHOICES, default=1)
    prioridad_numerica = models.IntegerField(null=False, default=1)
    proyecto = models.ForeignKey(Proyec, on_delete=models.CASCADE, blank=True, null=True, related_name="proyecto")
    aprobado_PB=models.BooleanField(default=False)
    sprint_backlog=models.BooleanField(default=False)
    estimacion_user=models.PositiveIntegerField(editable=True, default=0)
    estimacion_scrum = models.PositiveIntegerField(editable=True, default=0)


    def save(self, *args, **kwargs): # redefinicion del metodo save() que contiene nuestro trigger
        # Aqui ponemos el codigo del trigger -------
        if (self.prioridad=='Baja'):
            self.prioridad_numerica=1
        elif (self.prioridad=='Media'):
            self.prioridad_numerica=2
        elif (self.prioridad=='Alta'):
            self.prioridad_numerica=3
        super(HistoriaUsuario,self).save(*args,**kwargs)
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


def definir_estadoanterior(sender, instance, **kwargs):
    x = Proyec.objects.filter(id=instance.id).update(estado_anterior=instance.estado)


def agregar_fecha_inicio(sender, instance, **kwargs):
    if instance.estado != instance.estado_anterior:
        if instance.estado == 'Iniciado':
            x = Proyec.objects.filter(id=instance.id).update(fecha_inicio=instance.fecha)
        elif instance.estado == 'Cancelado':
            x = Proyec.objects.filter(id=instance.id).update(fecha_cancelado=instance.fecha)
        elif instance.estado == 'Concluido':
            x = Proyec.objects.filter(id=instance.id).update(fecha_concluido=instance.fecha)



def calcular_estimacion(sender, instance, **kwargs):
    if (instance.estimacion==0 and  instance.estimacion_scrum!=0 and instance.estimacion_user!=0):
        x=(instance.estimacion_scrum+instance.estimacion_user)/2
        HistoriaUsuario.objects.filter(id=instance.id).update(estimacion=x)


def agregar_encargado(sender, instance, **Kwargs):
    """ Funcion para agregar el encargado al equipo de trabajo cuando se crea un nuevo proyecto
        Además asigna al encargado el rol de Scrum Master
    Parametros:
        instance: Instancia del modelo a actualizar

    Retorna:
        Void. Solo modifica el modelo enviado
    """
    model = RolProyecto
    if not instance.equipo.all():
        instance.equipo.add(instance.encargado)
        nombreProyecto = instance.nombre
        nombreRol = "Scrum Master"
        rol = Rol(rol = f'{nombreRol}-{nombreProyecto}')
        user = instance.encargado
        print("USER", user)
        print(user.rol.filter(proyecto_id=instance.id).all())
        rol.save()
        print(rol.rol)
        print(rol.id)
        print(type(rol))
        rolProyecto = RolProyecto(nombre = rol.rol, proyecto=instance, rol = rol)
        rolProyecto.save()
        print(rolProyecto)
        user.rol.add(rolProyecto)
        grupo = Group.objects.filter(name=rol.rol).first()
        permiso1 = Permission.objects.get(codename='view_rol')
        permiso2 = Permission.objects.get(codename='add_rol')
        permiso3 = Permission.objects.get(codename='delete_rol')
        permiso4 = Permission.objects.get(codename='change_rol')
        permiso5 = Permission.objects.get(codename='delete_rol')
        permiso6 = Permission.objects.get(codename='view_historiausuario')
        permiso7 = Permission.objects.get(codename='delete_historiausuario')
        grupo.permissions.add(permiso1, permiso2, permiso3, permiso4, permiso5, permiso6, permiso7)
        user.groups.add(grupo)


pre_save.connect(definir_estadoanterior, sender=Proyec)
post_save.connect(agregar_fecha_inicio, sender=Proyec)
post_save.connect(calcular_estimacion, sender=HistoriaUsuario)
post_save.connect(agregar_encargado, sender=Proyec)
