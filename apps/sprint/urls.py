from django.urls import path
from .views import CrearSprint, ListarSprint, AgregarHU_sprint, EliminarSprint, EditarSprint

urlpatterns = [
     path('crear_sprint/<int:pk>',CrearSprint.as_view(),name='crear_sprint'),
     path('listar_sprint/<int:pk>',ListarSprint.as_view(),name='listar_sprint'),
     path('agregar_hu/<int:pk>',AgregarHU_sprint.as_view(),name='agregar_hu'),
     path('eliminar_sprint/<int:pk>',EliminarSprint.as_view(),name='eliminar_sprint'),
     path('editar_sprint/<int:pk>', EditarSprint.as_view(), name='editar_sprint'),
    ]