from django import forms
from django.contrib.auth.models import Permission, Group
from .models import User, Rol

class UserForm(forms.ModelForm):
    """ Formulario para usuario, se usa para crear los usuarios """
    class Meta:
        model = User
        fields = ['first_name', 'last_name','rol', 'email', 'is_active']
        labels = {
            'first_name': 'Nombre del usuario',
            'last_name': 'Apellidos del usuario',
            'rol': 'Rol del usuario',
            'email': 'correo del usuario',
            'is_active': 'Estado del usuario'
        }


class UserForm(forms.ModelForm):
    """ Formulario para asignar un rol a un usuario """
    class Meta:
        model = User
        fields = ['first_name', 'last_name','rol', 'email', 'is_active']
        labels = {
            'first_name': 'Nombre del usuario',
            'last_name': 'Apellidos del usuario',
            'rol': 'Rol del usuario',
            'email': 'correo del usuario',
            'is_active': 'Estado del usuario'
        }

class PermsForm(forms.ModelForm):
    """ Formulario para usuario, se usa para crear permisos """
    class Meta:
        model = Permission
        fields = ['codename', 'name', 'content_type']
        labels = {
            'codename': 'codename',
            'name': 'Nombre del permiso',
            'content_type': 'Tipo de contenido'
        }

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['rol']
        labels = {
            'Rol': 'Nombre del rol',
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['permissions']
        labels = {
            'permissions': 'Permisos del rol',
        }
        widgets = {
            'permissions': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }