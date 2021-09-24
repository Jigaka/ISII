from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.user.views import ListarUsuario, EliminarUsuario, \
    ActualizaUsuario, ActivosUsuario, ListarPermisos, \
    CrearPermisos, ListarRoles, CrearRoles, AgregarPermisosAlRol, AsignarRolUserProyecto, EliminarRol

urlpatterns = [
    path('listar_usuario/', login_required(ListarUsuario.as_view(), login_url='login'), name='listar_usuario'),
    path('listar_activos/', login_required(ActivosUsuario.as_view(), login_url='login'), name='listar_activos'),
    path('actualizar_usuario/<int:pk>/', login_required(ActualizaUsuario.as_view(), login_url='login'), name='actualizar_usuario'),
    path('eliminar_usuario/<int:pk>/', login_required(EliminarUsuario.as_view(), login_url='login'), name='eliminar_usuario'),
    path('listar_permisos/', ListarPermisos.as_view(), name='listar_permisos'),
    path('crear_permisos/', CrearPermisos.as_view(), name='crear_permisos'),
    path('listar_roles/<int:pk>', ListarRoles.as_view(), name='listar_roles'),
    path('crear_rol/<int:pk>', CrearRoles.as_view(), name='crear_rol'),
    path('eliminar_rol/<int:pk>', EliminarRol.as_view(), name='eliminar_rol'),
    path('asignar_rol/<int:pk>/<int:pl>', AsignarRolUserProyecto.as_view(), name='asignar_rol'),
    path('agregar_permisos_roles/<int:pk>/', AgregarPermisosAlRol.as_view(), name='agregar_permisos_roles'),
]
