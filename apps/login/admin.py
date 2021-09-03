from django.contrib import admin
from apps.login.models import ListaPermitidos


'''
Se muestra en la consola de administracion
la pestaña de ListaPermitos
'''
class ListaPermitidosAdmin(admin.ModelAdmin):
    list_display = ('id','correo')

admin.site.register(ListaPermitidos, ListaPermitidosAdmin)