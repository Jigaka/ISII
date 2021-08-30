from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('inicio')
    else:
        return HttpResponseRedirect('login')


