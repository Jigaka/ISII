from django.urls import path
from .views import CrearSprint

urlpatterns = [
     path('crear_sprint/<int:pk>',CrearSprint.as_view(),name='crear_sprint'),
    ]