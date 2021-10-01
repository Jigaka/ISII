from django.contrib import admin
from .models import Sprint
from .models import HistoriaUsuario
admin.site.register(HistoriaUsuario)
# Register your models here.
class SprintAdmin(admin.ModelAdmin):
    list_display=['nombre','proyecto','fecha_inicio','fecha_fin','estado','duracion_dias']
admin.site.register(Sprint, SprintAdmin)