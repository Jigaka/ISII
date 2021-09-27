from django import  forms
from django.forms.widgets import Widget
from .models import Proyec, Sprint, HistoriaUsuario
from datetime import date


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
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("fecha_inicio")
        end_date = cleaned_data.get("fecha_fin")
        if end_date <= start_date:
            raise forms.ValidationError('La fecha de fin debe ser mayor a la fecha de inicio')
        if date.today() > start_date:
            raise forms.ValidationError('¡La fecha de inicio no debe estar en el pasado!')
class agregar_hu_form(forms.ModelForm):
    class Meta:
        model=Sprint
        fields=['hu']
        #def __init__(self, *args, **kwargs):
        #    super(agregar_hu_form, self).__init__(*args, **kwargs)
        #    self.fields['hu'].queryset = HistoriaUsuario.objects.filter(aprobado_PB=True,sprint_backlog=False )
        labels = {
            'hu': 'seleccione Historia de Usuario'
        }

