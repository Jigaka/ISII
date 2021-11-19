from django.urls import path
from apps.proyectos.views import ConfigurarUs, estimarUS,Listar_us_a_estimar, Reasignar_us
from .views import AsignarCapacidadDiaria, CrearSprint, ListarSprint, AgregarHU_sprint, VerSprint, SprintBacklog, \
     configurarEquipoSprint, \
     Cambio_de_estadoHU, TablaKanban, EliminarSprint, EditarSprint, ListarEquipo, AddActividad, VerActividad, \
     Historial_por_hu, \
     VisualizarCapacidad, VerUS, AprobarQA, RechazarQA, BurnDownChart, Cancelar_hu, ReporteSprintBacklog, \
     ReporteSprintActual, IniciarSprint, SolicitarFinalizarSprint, FinalizarSprint, ListarActividades

urlpatterns = [
     path('crear_sprint/<int:pk>', CrearSprint.as_view(), name='crear_sprint'),
     path('listar_sprint/<int:pk>', ListarSprint.as_view(), name='listar_sprint'),
     path('agregar_hu/<int:pk>', AgregarHU_sprint.as_view(), name='agregar_hu'),
     path('ver_sprint/<int:pk>', VerSprint.as_view(), name='ver_sprint'),
     path('iniciar_sprint/<int:pk>', IniciarSprint.as_view(), name='iniciar_sprint'),
     path('ver_sb/<int:pk>', SprintBacklog.as_view(), name='ver_sb'),
     path('configurar_equipo/<int:pk>', configurarEquipoSprint.as_view(), name='configurar_equipo'),
     path('configurar_us/<int:pk>', ConfigurarUs.as_view(), name='configurar_us'),
     path('cambio_estadoHU/<int:pk>', Cambio_de_estadoHU.as_view(), name='cambio_estadoHU'),
     path('kanban/<int:pk>', TablaKanban.as_view(), name='kanban'),
     path('eliminar_sprint/<int:pk>',EliminarSprint.as_view(),name='eliminar_sprint'),
     path('editar_sprint/<int:pk>', EditarSprint.as_view(), name='editar_sprint'),
     path('solicitar_finalizar_sprint/<int:pk>',SolicitarFinalizarSprint.as_view(), name='solicitar_finalizar_sprint'),
     path('finalizar_sprint/<int:pk>',FinalizarSprint.as_view(), name='finalizar_sprint'),
     path('listar_equipo/<int:pk>', ListarEquipo.as_view(), name='listar_equipo'),
     path('cargar_capacidad/<int:pk>/<int:pk2>', AsignarCapacidadDiaria.as_view(), name='asignar_capacidad'),
     path('listar_us_a_estimar_us/<int:pk>',Listar_us_a_estimar.as_view(), name='listar_us_a_estimar'),
     path('estimar_us/<int:pk>',estimarUS.as_view(), name='estimar_us'),
     path('add_actividad/<int:pk>/<int:us>',AddActividad.as_view(), name='add_actividad'),
     path('aprobarQA/<int:pk>/<int:us>',AprobarQA.as_view(), name='aprobarQA'),
     path('rechazarQA/<int:pk>/<int:us>',RechazarQA.as_view(), name='rechazarQA'),
     path('ver_actividad/<int:pk>',VerActividad.as_view(), name='ver_actividad'),
     path('listar_actividades/<int:pk>',ListarActividades.as_view(), name='listar_actividades'),
     path('historial_hu/<int:pk>',Historial_por_hu.as_view(), name='historial_hu'),
     path('reasignar_us/<int:pk>',Reasignar_us.as_view(), name='reasignar_us'),
     path('ver_us/<int:pk>/<int:pl>',VerUS.as_view(), name='ver_us'),
     path('capacidad/<int:pk>',VisualizarCapacidad.as_view(), name='capacidad'),
     path('burn_down_chart/<int:pk>',BurnDownChart.as_view(), name='burn_down_chart'),
     path('cancelar_hu/<int:pk>',Cancelar_hu.as_view(), name='cancelar_hu'),
     path('reporte_SB/<int:pk>',ReporteSprintBacklog.as_view(), name='reporte_SB'),
     path('reporte_SA/<int:pk>',ReporteSprintActual.as_view(), name='reporte_SA'),

    ]
