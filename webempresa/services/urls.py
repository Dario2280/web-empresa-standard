from django.urls import path
from . import views #Importamos la view de services

# aqui redefinimos nuestra url para la seccion servicios
urlpatterns = [

    path('services', views.services, name="services"),
 
]