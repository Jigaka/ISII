from django import  forms
from django.forms.widgets import Widget
from .models import Proyec, Sprint, HistoriaUsuario
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
class DateInput(forms.DateInput):
    input_type='date'
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
        #if (estado == Iniciado):
        #fecha_inicio = forms.DateField("fecha_de_creacion", auto_now=True, auto_now_add=False)


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
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("fecha_inicio")
        end_date = cleaned_data.get("fecha_fin")
        if end_date <= start_date:
            raise forms.ValidationError('La fecha de fin debe ser mayor a la fecha de inicio')
        if date.today() > start_date:
            raise forms.ValidationError('¡La fecha de inicio no debe estar en el pasado!')

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
            'aprobado_PB': 'Aprobar Historia de Usuario'
        }