from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.user.views import Inicio, logout_Usuario
from apps.login.views import index



urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', TemplateView.as_view(template_name="login/login.html"),name='login'),
    path('accounts/', include('allauth.socialaccount.providers.google.urls')),
    path('inicio/',login_required(Inicio.as_view(),login_url='login'), name = 'inicio'),
    path('usuarios/',include(('apps.user.urls','usuarios'))),
    path('login/',include(('apps.login.urls','login'))),
    path('logout/',logout_Usuario, name = 'logout'),
    path('proyectos/', include(('apps.proyectos.urls', 'proyectos'))),
    path('sprint/', include(('apps.sprint.urls', 'sprint')))
]
