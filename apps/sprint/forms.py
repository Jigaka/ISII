from django import forms
from .models import CapacidadDiariaEnSprint, Proyec, Sprint, HistoriaUsuario, Actividad,Estado_HU
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
    def __init__(self, pk, id_sprint,*args, **kwargs):
        self.id_proyecto= pk
        self.id_sprint= id_sprint
        super(SprintForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("fecha_inicio")
        end_date = cleaned_data.get("fecha_fin")
        if end_date <= start_date:
            raise forms.ValidationError('¡La fecha de fin no puede ser menor a la fecha de inicio!')
        if date.today() > start_date:
            raise forms.ValidationError('¡La fecha de inicio no puede estar en el pasado!')

        #raise forms.ValidationError(self.id_proyecto)

        sprints=Sprint.objects.filter(proyecto__id=self.id_proyecto).exclude(id=self.id_sprint)
        #raise forms.ValidationError(str(self.id_proyecto)+"    "+str(self.id_sprint))
        #raise forms.ValidationError(self.id_proyecto) #levanto este error en pruebas para ver qué id guardó
        for e in sprints:
            if (start_date < e.fecha_inicio):
                if (end_date == e.fecha_inicio):
                    raise forms.ValidationError("¡Sprint solapado! La fecha de finalización asignada es la fecha de inicio de otro Sprint.")
                if (end_date > e.fecha_inicio):
                    raise forms.ValidationError("¡Sprint solapado! La fecha de finalización asignada se encuentra dentro del intervalo de otro Sprint.")
            elif (start_date == e.fecha_inicio):
                raise forms.ValidationError("¡Sprint solapado! Esta fecha de inicio ya ha sido asignada a otro Sprint.")
            elif (start_date > e.fecha_inicio):
                if (start_date<=e.fecha_fin):
                    raise forms.ValidationError("¡Sprint solapado!")
class agregar_hu_form(forms.ModelForm):
    '''funcion para que filtre solo los sprints de un proyecto en especifico'''
    class Meta:
        model = HistoriaUsuario
        fields = ['sprint']
        labels = {
            'sprint': 'Seleccione un sprint'
        }
    def __init__(self,*args, **kwargs):
        super(agregar_hu_form, self).__init__(*args, **kwargs)
        HU=HistoriaUsuario.objects.get(nombre=kwargs.get('instance'))
        # se quita estado pendiente por el momento
        # Todo volver a poner estado pendiente
        self.fields['sprint'].queryset = Sprint.objects.filter(proyecto_id=HU.proyecto.id,estado="Pendiente")


class CrearActividadForm(forms.ModelForm):
    '''
        Actividad realizada en una historia de usuario
    '''
    fecha = forms.DateField(widget=DateInput)

    class Meta:
        model = Actividad
        fields = ['nombre', 'comentario','fecha', 'hora_trabajo']
        labels = {
            'nombre' : 'Nombre de la actividad',
            'comentario' : 'Escribe un breve comentario',
            'fecha': 'ingrese la fecha de la actividad',
            'hora_trabajo' : 'Horas trabajadas'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una actividad'
                }
            ),
            'comentario': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese un comentario'
                }
            ),

        }

class configurarEquipoSprintform(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['equipo']
        labels = {
            'equipo': 'Seleccione los integrantes del equipo de este Sprint'

        }
    def __init__(self, *args, **kwargs):
        super(configurarEquipoSprintform, self).__init__(*args, **kwargs)
        sprint = Sprint.objects.get(nombre=kwargs.get('instance'))
        self.fields['equipo'].queryset = Proyec.objects.get(id=sprint.proyecto_id).equipo

class cambio_estadoHU_form(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['estado']
        labels = {
            'estado': 'Seleccione estado de la Historia de Usuario'
        }

class CapacidadDiariaEnSprintForm(forms.ModelForm):
    capacidad_diaria_horas=forms.IntegerField()
    class Meta:
        model=CapacidadDiariaEnSprint
        fields=['capacidad_diaria_horas']
        labels = {
            'capacidad_diaria_horas': 'Capacidad diaria (horas)'
        }

class aprobarQAForm(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['aprobado_QA', 'comentario']
        labels = {
            'aprobado_QA': 'Aprobar Historia de Usuario ',
            'comentario':'Comentario'
        }

class rechazarQAForm(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['rechazado_QA','comentario']
        labels = {
            'rechazado_QA': 'Rechazar Historia de Usuario ',
            'comentario': 'Comentario'
        }

class cancelar_huform(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = ['cancelado']
        labels = {
            'cancelado': 'Cancelar esta historia de usuario'
        }

