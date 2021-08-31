from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active']
        labels = {
            'first_name': 'Nombre del usuario',
            'last_name': 'Apellidos del usuario',
            'email': 'correo del usuario',
            'is_active': 'Estado del usuario'
        }