from django.urls import path
from .views import crearProyecto, listarProyectos, editarProyecto, eliminarProyecto
from apps.user.views import listarProyectoporUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_proyecto/',login_required(crearProyecto, login_url='login'), name='crear_proyecto'),
    path('listar_proyectos/',login_required(listarProyectos, login_url='login'), name='listar_proyectos'),
    path('editar_proyectos/<int:id>',login_required(editarProyecto, login_url='login'), name='editar_proyectos'),
    path('eliminar_proyectos/<int:id>',login_required(eliminarProyecto, login_url='login'), name='eliminar_proyectos'),
    path('mis_proyectos/',login_required(listarProyectoporUsuario, login_url='login'), name='mis_proyectos')
]