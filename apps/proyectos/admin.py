from django.contrib import admin

# Register your models here.
from .models import Proyec, RolProyecto, Sprint


class RolProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


# Register your models here.
admin.site.register(Proyec)
admin.site.register(RolProyecto,RolProyectoAdmin)
admin.site.register(Sprint)