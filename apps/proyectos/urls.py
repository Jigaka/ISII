from django.urls import path
from .views import CrearProyecto, ListarProyectos, EditarProyecto, EliminarProyecto
from apps.user.views import listarProyectoporUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_proyecto/',CrearProyecto.as_view(), name='crear_proyecto'),
    path('listar_proyectos/',ListarProyectos.as_view(), name='listar_proyectos'),
    path('editar_proyecto/<int:pk>/',EditarProyecto.as_view(), name='editar_proyecto'),
    path('eliminar_proyecto/<int:pk>/',EliminarProyecto.as_view(), name='eliminar_proyecto'),
    path('mis_proyectos/',login_required(listarProyectoporUsuario, login_url='login'), name='mis_proyectos')
]