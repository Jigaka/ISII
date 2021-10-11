from django import  forms
from django.forms.widgets import Widget
from .models import Proyec
from apps.user.models import User
from apps.sprint.models import HistoriaUsuario, Sprint

from datetime import date
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
class configurarUSform(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['estimacion_scrum','asignacion']
        labels = {
            'estimacion_scrum': 'estimacion de tiempo para la historia de usuario',
            'asignacion':'Asignar Historia de Usuario'
        }
    def __init__(self, *args, **kwargs):
        super(configurarUSform, self).__init__(*args, **kwargs)
        sprint = HistoriaUsuario.objects.get(nombre=kwargs.get('instance')).sprint
        #print(HU)
        self.fields['asignacion'].queryset = Sprint.objects.get(id=sprint.id).equipo

class estimar_userform(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['estimacion_user']
        labels = {
            'estimacion_user': 'estimacion de tiempo para la historia de usuario',
        }


class aprobar_usform(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['aprobado_PB']
        labels = {
            'aprobado_PB': 'Aprobar Historia de Usuario '
        }