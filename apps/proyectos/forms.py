from django import  forms
from django.forms.widgets import Widget
from .models import Proyec, Sprint

'''
Form para rellenar campos para la creacion y/o edicion
de un proyecto
'''
class ProyectoForm(forms.ModelForm):
    estado=forms.ChoiceField(choices=Proyec.STATUS_CHOICES)
    class Meta:
        model= Proyec
        fields=['nombre', 'equipo', 'descripcion','estado']
        labels = {
            'nombre': 'Nombre del proyecto',
            'equipo': 'Miembros del proyecto',
            'descripcion': 'Descripcion del proyecto',
            'estado': 'Estado del proyecto',
        }
        #if (estado == Iniciado):
        #fecha_inicio = forms.DateField("fecha_de_creacion", auto_now=True, auto_now_add=False)

class DateInput(forms.DateInput):
    input_type='date'
    
class SprintForm(forms.ModelForm):
    fecha_inicio=forms.DateField(widget=DateInput)
    fecha_fin=forms.DateField(widget=DateInput)
    class Meta:
        model=Sprint
        fields=['nombre','fecha_inicio','fecha_fin']
        labels = {
            'nombre': 'Nombre',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_fin': 'Fecha de finalización'
        }