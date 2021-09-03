from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

'''
Metodo que muestra al usuario
la pantalla de inicio en que de estar logueado, 
sino muestra la pantalla de inicio de sesion
'''
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('inicio')
    else:
        return HttpResponseRedirect('login')


