from django.contrib import admin
from .models import ListaPermitidos


class ListaPermitidosAdmin(admin.ModelAdmin):
    list_display = ('id','correo')

admin.site.register(ListaPermitidos, ListaPermitidosAdmin)