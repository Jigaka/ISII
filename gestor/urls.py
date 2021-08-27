from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.user.views import inicio, logout_Usuario

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('inicio/',login_required(inicio), name = 'inicio'),
    path('logout/',logout_Usuario, name = 'logout')
]
