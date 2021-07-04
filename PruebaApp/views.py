from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hola mundo")


def harry(request):
    return HttpResponse("hola harry")


def hola(request, nombre):
    return HttpResponse(f"hola, {nombre.capitalize()}!")
    
def plantilla(request):
    return render(request, "hola/index.html")