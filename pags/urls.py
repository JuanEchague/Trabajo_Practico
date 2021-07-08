from django.urls import path
from . import views

urlpatterns = [
     path('pag1', views.pag1, name="pag1"),
    path('pag2', views.pag2, name="pag2"),
    path('pag3', views.pag3, name="pag3"),
    path('crear_usuario', views.crear_usuario, name="crear_usuario"),
    path('busqueda', views.busqueda, name="busqueda"),
    path('producto', views.producto, name="producto"),
    path('nuevo_producto', views.nuevo_producto, name="nuevo_producto"),
    path('editar_producto', views.editar_producto, name="editar_producto"),
    path('carrito', views.carrito, name="carrito"),
]
