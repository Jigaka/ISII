from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.contrib.auth.models import Permission, Group
from django.db.models.signals import post_save, pre_save
from django.template.loader import get_template
from django.conf import settings
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



def agregar_fecha(sender, instance, **kwargs):
    if instance.estado != instance.estado_anterior:
        if instance.estado == 'Iniciado':
            Proyec.objects.filter(id=instance.id).update(fecha_inicio=instance.fecha,estado_anterior=instance.estado)
        elif instance.estado == 'Cancelado':
            Proyec.objects.filter(id=instance.id).update(fecha_cancelado=instance.fecha, estado_anterior=instance.estado)
        elif instance.estado == 'Concluido':
            Proyec.objects.filter(id=instance.id).update(fecha_concluido=instance.fecha, estado_anterior=instance.estado)
        
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
        #print("USER", user)
        #print(user.rol.filter(proyecto_id=instance.id).all())
        rol.save()
        #print(rol.rol)
        #print(rol.id)
        #print(type(rol))
        rolProyecto = RolProyecto(nombre = rol.rol, proyecto=instance, rol = rol)
        rolProyecto.save()
        #print(rolProyecto)
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
        id = instance.id
        idp= instance.encargado.id
        u=User.objects.get(id=idp)
        context = {'proyecto': Proyec.objects.get(id=id)}
        template = get_template('correos/encargado.html')
        content = template.render(context)
        email = EmailMultiAlternatives('Notificacion Apepu Gestor', 'Notificacion', settings.EMAIL_HOST_USER,
                                       [user.getEmail()])
        email.attach_alternative(content, 'text/html')
        email.send()
        user.groups.add(grupo)

post_save.connect(agregar_fecha, sender=Proyec)
post_save.connect(agregar_encargado, sender=Proyec)