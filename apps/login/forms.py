from django import forms
from .models import ListaPermitidos

class CorreoForm(forms.ModelForm):
    class Meta:
        model = ListaPermitidos
        fields = ['correo']
        widgets = {
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un correo',
                }
            ),
        }