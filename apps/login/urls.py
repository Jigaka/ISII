from django.urls import path
from apps.login.views import  AgregarCorreosPermitidos, ListarCorreosPermitidos, EliminarCorreosPermitidos

urlpatterns = [
    path('agregar_correos_permitidos/', AgregarCorreosPermitidos.as_view(), name = 'agregar_correos_permitidos'),
    path('listar_correos_permitidos/', ListarCorreosPermitidos.as_view(), name = 'listar_correos_permitidos'),
    path('eliminar_correos_permitidos/<int:pk>/', EliminarCorreosPermitidos.as_view(), name = 'eliminar_correos_permitidos'),

]