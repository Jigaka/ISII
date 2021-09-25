from django.contrib import admin

# Register your models here.
from .models import Proyec, RolProyecto, Sprint
from .models import HistoriaUsuario


class RolProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class SprintAdmin(admin.ModelAdmin):
    list_display=['nombre','proyecto','fecha_inicio','fecha_fin','duracion_dias']

# Register your models here.
admin.site.register(Proyec)
admin.site.register(RolProyecto,RolProyectoAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(HistoriaUsuario)