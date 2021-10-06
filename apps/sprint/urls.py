from django.urls import path
from .views import CrearSprint, ListarSprint, AgregarHU_sprint, VerSprint, SprintBacklog, configurarEquipoSprint, \
     Cambio_de_estadoHU, TablaKanban, ListarEquipo
from apps.proyectos.views import ConfigurarUs

urlpatterns = [
     path('crear_sprint/<int:pk>', CrearSprint.as_view(), name='crear_sprint'),
     path('listar_sprint/<int:pk>', ListarSprint.as_view(), name='listar_sprint'),
     path('agregar_hu/<int:pk>', AgregarHU_sprint.as_view(), name='agregar_hu'),
     path('ver_sprint/<int:pk>', VerSprint.as_view(), name='ver_sprint'),
     path('ver_sb/<int:pk>', SprintBacklog.as_view(), name='ver_sb'),
     path('configurar_equipo/<int:pk>', configurarEquipoSprint.as_view(), name='configurar_equipo'),
     path('configurar_us/<int:pk>', ConfigurarUs.as_view(), name='configurar_us'),
     path('cambio_estadoHU/<int:pk>', Cambio_de_estadoHU.as_view(), name='cambio_estadoHU'),
     path('kanban/<int:pk>', TablaKanban.as_view(), name='kanban'),
     path('listar_equipo/<int:pk>', ListarEquipo.as_view(), name='listar_equipo'),
    ]
