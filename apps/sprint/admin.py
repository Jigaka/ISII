from django.contrib import admin
from .models import Sprint
# Register your models here.
class SprintAdmin(admin.ModelAdmin):
    list_display=['nombre','proyecto','fecha_inicio','fecha_fin','duracion_dias']
admin.site.register(Sprint, SprintAdmin)