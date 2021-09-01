from django import  forms
from .models import Proyec

class ProyectoForm(forms.ModelForm):
    estado=forms.ChoiceField(choices=Proyec.STATUS_CHOICES)
    class Meta:
        model= Proyec
        fields=['nombre', 'equipo', 'descripcion','estado']
        #if (estado == Iniciado):
        #fecha_inicio = forms.DateField("fecha_de_creacion", auto_now=True, auto_now_add=False)