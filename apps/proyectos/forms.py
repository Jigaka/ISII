from django import forms
from .models import Proyec, HistoriaUsuario

'''
Form para rellenar campos para la creacion y/o edicion
de un proyecto
'''
class ProyectoForm(forms.ModelForm):

    class Meta:
        model= Proyec

        fields=['nombre', 'descripcion','encargado']
        labels = {
            'nombre': 'Nombre del proyecto',
            'encargado':'Encargado del Proyecto',
            'descripcion': 'Descripcion del proyecto',

        }
class editarProyect(forms.ModelForm):
    class Meta:
        model = Proyec
        fields = ['nombre', 'descripcion','estado','equipo','dias_estimados']
        labels = {
            'nombre': 'Nombre del proyecto',
            'descripcion': 'Descripcion del proyecto',
            'estado': 'Estado del proyecto',
            'equipo':'Equipo de trabajo',
            'dias_estimados':'Cantdad de dias estimados'
        }

class CrearUSForm(forms.ModelForm):
    class Meta:
        model= HistoriaUsuario
        fields=['nombre', 'descripcion','prioridad']
        labels = {
            'nombre': 'Nombre de la Historia de Usuario',
            'descripcion': 'Descripcion de la Historia de Usuario',
            'prioridad':'Prioridad de la Historia de Usuario'
        }
class editarUS(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['nombre', 'descripcion', 'prioridad','estado','estimacion','asignacion']
        labels = {
            'nombre': 'Nombre de la Historia de Usuario',
            'descripcion': 'Descripcion de la Historia de Usuario',
            'prioridad': 'Prioridad de la Historia de Usuario',
            'estado': 'Estado de la Historia de Usuario',
            'asignacion':'Asignar Historia de Usuario'
        }
