from django import  forms
from django.forms.widgets import Widget
from .models import Proyec
from apps.user.models import User
from apps.sprint.models import HistoriaUsuario, Sprint, Actividad

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
        fields = ['nombre', 'descripcion','dias_estimados']
        labels = {
            'nombre': 'Nombre del proyecto',
            'descripcion': 'Descripcion del proyecto',
            'dias_estimados':'Cantdad de dias estimados'
        }

class cambiarEstadoProyect(forms.ModelForm):
    class Meta:
        model = Proyec
        fields = ['estado']
        labels = {
            'estado': 'Estado del proyecto',
        }        

class asignarEquipoProyect(forms.ModelForm):
    class Meta:
        model = Proyec
        fields = ['equipo']
        labels = {
             'equipo':'Equipo de trabajo',
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
            'estimacion_scrum': 'Tiempo requerido (en horas)',
            'asignacion':'Asignar Historia de Usuario'
        }

    def __init__(self, *args, **kwargs):
        super(configurarUSform, self).__init__(*args, **kwargs)
        sprint = HistoriaUsuario.objects.get(nombre=kwargs.get('instance')).sprint
        #print(HU)
        self.fields['asignacion'].queryset = Sprint.objects.get(id=sprint.id).equipo
    
    def clean(self):
        cleaned_data = super().clean()
        estimacion_scrum = cleaned_data.get('estimacion_scrum')
        if (estimacion_scrum <= 0):
            raise forms.ValidationError('Por favor inserte un número positivo.')


class reasignarUSform(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['asignacion']
        labels = {
            'asignacion': 'Asignar desarrollador'
        }
    def __init__(self, *args, **kwargs):
        super(reasignarUSform, self).__init__(*args, **kwargs)
        sprint = HistoriaUsuario.objects.get(nombre=kwargs.get('instance')).sprint
        # print(HU)
        self.fields['asignacion'].queryset = Sprint.objects.get(id=sprint.id).equipo



class estimar_userform(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['estimacion_user']
        labels = {
            'estimacion_user': 'Tiempo requerido (en horas)',
        }
    def clean(self):
        cleaned_data = super().clean()
        estimacion_user = cleaned_data.get('estimacion_user')
        if (estimacion_user <= 0):
            raise forms.ValidationError('Por favor inserte un número positivo.')
    


class aprobar_usform(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['aprobado_PB']
        labels = {
            'aprobado_PB': 'Aprobar Historia de Usuario '
        }

class rechazar_usform(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['rechazado_PB']
        labels = {
            'rechazado_PB': 'Rechazar Historia de Usuario '
        }