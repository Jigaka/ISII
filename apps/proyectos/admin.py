from django.contrib import admin

# Register your models here.
from .models import Proyec, RolProyecto, RolProyectoUsuario

# Register your models here.
admin.site.register(Proyec)
admin.site.register(RolProyecto)
admin.site.register(RolProyectoUsuario)