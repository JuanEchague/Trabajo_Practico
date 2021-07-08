from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pag1(request):
    return render(request, "pag1/index.html") 

def pag2(request):
    return render(request, "pag1/AcercaDe.html")

def pag3(request):
    return render(request, "pag1/login.html")

def crear_usuario(request):
    return render(request, "pag1/crear_usuario.html")

def busqueda(request):
    return render(request, "pag1/busqueda.html")

def producto(request):
    return render(request, "pag1/producto.html")

def nuevo_producto(request):
    return render(request, "pag1/nuevo_producto.html")

def editar_producto(request):
    return render(request, "pag1/editar_producto.html")

def carrito(request):
    return render(request, "pag1/carrito.html")