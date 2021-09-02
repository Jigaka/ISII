from django.urls import path
from .views import crearProyecto, listarProyectos, editarProyecto, eliminarProyecto
from apps.user.views import listarProyectoporUsuario

urlpatterns = [
    path('crear_proyecto/',crearProyecto, name='crear_proyecto'),
    path('listar_proyectos/',listarProyectos, name='listar_proyectos'),
    path('editar_proyectos/<int:id>',editarProyecto, name='editar_proyectos'),
    path('eliminar_proyectos/<int:id>',eliminarProyecto, name='eliminar_proyectos'),
    path('mis_proyectos/',listarProyectoporUsuario, name='mis_proyectos')
]