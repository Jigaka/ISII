from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType

class Rol(models.Model):
    """Modelo para el rol"""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    rol = models.CharField('Rol', max_length=50, unique=True)

    class Meta:
        """Meta definition for Rol."""
        verbose_name = 'Rol'
        verbose_name_plural = 'Rols'

    def __str__(self):
        """Unicode representation of Rol."""
        return self.rol

    def save(self, *args, **kwargs):
        """ Se llama cada vez que se crea un rol, y crea un grupo asociado al rol, se crea con el mismo nombre"""
        permisos_defecto = ['add', 'change', 'delete', 'view']
        if not self.id:
            nuevo_grupo, creado = Group.objects.get_or_create(name=f'{self.rol}')
            for permiso_temp in permisos_defecto:
                permiso, created = Permission.objects.update_or_create(
                    name=f'Can {permiso_temp} {self.rol}',
                    content_type=ContentType.objects.get_for_model(Rol),
                    codename=f'{permiso_temp}_{self.rol}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args, **kwargs)
        else:
            rol_antiguo = Rol.objects.filter(id=self.id).values('rol').first()
            if rol_antiguo['rol'] == self.rol:
                super().save(*args, **kwargs)
            else:
                Group.objects.filter(name=rol_antiguo['rol']).update(name=f'{self.rol}')
                for permiso_temp in permisos_defecto:
                    Permission.objects.filter(codename=f"{permiso_temp}_{rol_antiguo['rol']}").update(
                        codename=f'{permiso_temp}_{self.rol}',
                        name=f'Can {permiso_temp} {self.rol}'
                    )
                super().save(*args, **kwargs)

class User(AbstractUser):
    rol = models.ManyToManyField('proyectos.RolProyecto', related_name='user_rol_proyecto')
    def getIdUsuario(self):
        return self.id

    def getNombreUsuario(self):
        return self.username

    def getNombre(self):
        return self.first_name

    def getApellido(self):
        return self.last_name

    def getEmail(self):
        return self.email

    def save(self, *args, **kwargs):
        """Esta función se llama cada vez que se le asigna un rol a un usuario para asociarle el grupo correspondiente.
            Si se le asigna un nuevo rol, se remueve el grupo anterior y se le agrega el nuevo grupo
        """
        if kwargs.get('pl') != None:
            print('1111111111111111111111111111111111111')
            print('1111111111111111111111111111111111111')
            idProyecto = self.rol.filter(proyecto_id=kwargs['pl']).first().rol.id
            rolProyecto = self.rol.filter(proyecto_id=kwargs['pl']).first().rol.rol
            if not idProyecto:
                print("MMMMMMMMMMMMM")
                super().save(*args, **kwargs)
                if rolProyecto is not None:
                    grupo =  Group.objects.filter(name=self.rol.filter(proyecto_id=kwargs['pl']).first().rol.rol).first()
                    if grupo:
                        self.groups.add(grupo)
                        print("POR AQUI")
                        super().save(*args, **kwargs)
            else:

                if self.rol is not None:
                    rol_proyecto = self.rol.filter(proyecto_id=kwargs['pl']).first() #rol por proyecto
                    usuario = User.objects.get(id=kwargs['pk']) #id del usuario
                    usuario2 = User.objects.filter(id=self.id)
                    rol = usuario.rol.filter(proyecto_id=kwargs['pl']).first() #id del proyecto
                    grupo_antiguo_lista = User.objects.filter(id=kwargs['pk']).values('rol__nombre').all() #En grupo_antiguo_lista guarda todos los roles que tiene el usuario
                    print("Grupo antiguo+++++",User.objects.filter(id=kwargs['pk']).values('rol__nombre').all())
                    usu = User.objects.filter(id=kwargs['pk']).values('rol__nombre')
                    print("Grupo del forms")
                    print(self.rol.filter(proyecto_id=kwargs['pl']).first().rol.rol)
                    print("LISTAAAAAAAAAAAA")
                    lista = User.objects.filter(id=kwargs['pk']).values('rol')
                    lista = User.objects.filter(id=kwargs['pk'])
                    print(lista)

                    id_grupo = self.rol.filter(proyecto_id=kwargs['pl']).first().id  #se obtiene el id del grupo relacionado con el rol
                    nombre_grupo = self.rol.filter(proyecto_id=kwargs['pl']).first().nombre # se obtiene el nombre del grupo apartir del nombre del rol
                    print("GRUU", id_grupo)
                    print(type(grupo_antiguo_lista))

                    """"En esta parte se verifica si el usuario ya tiene asignado el grupo
                            si exite no pasa nada
                            si no existe el grupo se le agrega al usuario
                    """
                    if grupo_antiguo_lista.filter(groups=id_grupo).exists():
                        print("EXISTE")
                        print(Group.objects.filter(id = id_grupo))
                        print(nombre_grupo)
                    else:
                        print("No existe")
                        nuevo_grupo = Group.objects.filter(name=self.rol.filter(proyecto_id=kwargs['pl']).first().rol.rol).first()
                        print("NUEVOOOO")
                        print(nuevo_grupo)
                        self.groups.add(nuevo_grupo)
                    ############################################################################################

        else:
            super().save(*args, **kwargs)
