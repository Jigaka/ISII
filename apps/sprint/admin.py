from django.contrib import admin
from .models import Sprint, HistoriaUsuario, CapacidadDiariaEnSprint, Historial_HU, Actividad

# Register your models here.

admin.site.register(HistoriaUsuario)
admin.site.register(Historial_HU)
class SprintAdmin(admin.ModelAdmin):
    list_display=['nombre','proyecto','fecha_inicio','fecha_fin','estado','duracion_dias','duracion_cruda']
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Actividad)
admin.site.register(CapacidadDiariaEnSprint)
