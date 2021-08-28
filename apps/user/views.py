from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.

def inicio(request):#para toda peticion proveniente del navegador debe usarse request
    return render(request,'inicio.html')


def logout_Usuario(request):
    logout(request)
    return HttpResponseRedirect('/')
