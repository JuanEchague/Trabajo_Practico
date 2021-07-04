from django.urls import path
from . import views

urlpatterns = [
    path('pag1', views.pag1, name="pag1"),
    path('pag2', views.pag2, name="pag2"),
    path('pag3', views.pag3, name="pag3"),
]
