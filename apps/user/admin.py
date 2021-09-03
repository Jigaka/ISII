from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import User
from apps.user.models import Rol
# Register your models here.

admin.site.register(Permission)
admin.site.register(User)
admin.site.register(Rol)
