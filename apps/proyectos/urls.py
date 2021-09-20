from django.urls import path
from django.views.generic import TemplateView
from .views import CrearProyecto, ListarProyectos, EditarProyecto, EliminarProyecto, ConfigurarUs,Proyecto, ListadoIntegrantes, listarProyectosUsuario,listarProyectoporEncargado, CrearUS, EditarUs, ListarUS,EliminarUS, aprobarUS,ProductBacklog
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_proyecto/',CrearProyecto.as_view(), name='crear_proyecto'),
    path('listar_proyectos/',ListarProyectos.as_view(), name='listar_proyectos'),
    path('editar_proyecto/<int:pk>/',EditarProyecto.as_view(), name='editar_proyecto'),
    path('eliminar_proyecto/<int:pk>/',EliminarProyecto.as_view(), name='eliminar_proyecto'),
    path('listar_integrantes/<int:pk>',ListadoIntegrantes.as_view(), name='listar_integrantes'),
    # path('asignar_roles/<int:pk>/',AsignarRolProyecto.as_view(), name='asignar_roles'),
    path('mis_proyectos/', listarProyectosUsuario.as_view(), name='mis_proyectos'),
    path('proyectos_por_encargado/', listarProyectoporEncargado, name='mis_proyectos(encargado)'),
    path('ver_proyecto/<int:pk>', Proyecto.as_view(), name='ver_proyecto'),
    path('crear_us/<int:pk>',CrearUS.as_view(),name='crear_us'),
    path('listar_us/<int:pk>', ListarUS.as_view(), name='listar_us'),
    path('editar_us/<int:pk>/', EditarUs.as_view(), name='editar_us'),
    path('configurar_us/<int:pk>/', ConfigurarUs.as_view(), name='configurar_us'),
    path('eliminar_us/<int:pk>/',EliminarUS.as_view(), name='eliminar_us'),
    path('aprobar_us/<int:pk>/',aprobarUS.as_view(), name='aprobar_us'),
    path('ver_PB/<int:pk>', ProductBacklog.as_view(), name='ver_pb'),

]