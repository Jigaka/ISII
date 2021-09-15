from django.urls import path
from django.views.generic import TemplateView

from .views import CrearProyecto, ListarProyectos, EditarProyecto, EliminarProyecto, Proyecto, ListadoIntegrantes
from apps.user.views import listarProyectoporUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_proyecto/',CrearProyecto.as_view(), name='crear_proyecto'),
    path('listar_proyectos/',ListarProyectos.as_view(), name='listar_proyectos'),
    path('editar_proyecto/<int:pk>/',EditarProyecto.as_view(), name='editar_proyecto'),
    path('eliminar_proyecto/<int:pk>/',EliminarProyecto.as_view(), name='eliminar_proyecto'),
    path('listar_integrantes/<int:pk>',ListadoIntegrantes.as_view(), name='listar_integrantes'),
    # path('asignar_roles/<int:pk>/',AsignarRolProyecto.as_view(), name='asignar_roles'),
    path('mis_proyectos/',login_required(listarProyectoporUsuario, login_url='login'), name='mis_proyectos'),
    path('loco/<int:pk>', Proyecto.as_view(), name='loco')
]