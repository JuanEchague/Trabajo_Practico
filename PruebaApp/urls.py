
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('harry', views.harry, name="harry"),
    path('saludar/<str:nombre>', views.hola, name="hola"),
    path('plantilla', views.plantilla, name="plantilla")

]
