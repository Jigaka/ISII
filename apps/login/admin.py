from django.contrib import admin
from apps.login.models import ListaPermitidos


class ListaPermitidosAdmin(admin.ModelAdmin):
    list_display = ('id','correo')

admin.site.register(ListaPermitidos, ListaPermitidosAdmin)