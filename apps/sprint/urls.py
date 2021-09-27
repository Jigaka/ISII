from django.urls import path
from .views import CrearSprint, ListarSprint, AgregarHU_sprint, VerSprint

urlpatterns = [
     path('crear_sprint/<int:pk>',CrearSprint.as_view(),name='crear_sprint'),
     path('listar_sprint/<int:pk>',ListarSprint.as_view(),name='listar_sprint'),
     path('agregar_hu/<int:pk>',AgregarHU_sprint.as_view(),name='agregar_hu'),
     path('ver_sprint/<int:pk>',VerSprint.as_view(),name='ver_sprint'),
    ]