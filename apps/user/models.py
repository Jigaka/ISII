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
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)
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
        if not self.id:
            super().save(*args, **kwargs)
            if self.rol is not None:
                grupo = Group.objects.filter(name=self.rol.rol).first()
                if grupo:
                    self.groups.add(grupo)
                super().save(*args, **kwargs)
        else:
            if self.rol is not None:
                grupo_antiguo = User.objects.filter(id=self.id).values('rol__rol').first()
                # print(grupo_antiguo['rol__rol'])
                # print(self.rol.rol)
                if grupo_antiguo['rol__rol'] == self.rol.rol:
                    print("Entro en igualdad de roles")
                    super().save(*args, **kwargs)
                else:
                    grupo_anterior = Group.objects.filter(name=grupo_antiguo['rol__rol']).first()
                    if grupo_anterior:
                        print(grupo_anterior)
                        self.groups.remove(grupo_anterior)
                    nuevo_grupo = Group.objects.filter(name=self.rol.rol).first()
                    if nuevo_grupo:
                        self.groups.add(nuevo_grupo)
                    super().save(*args, **kwargs)