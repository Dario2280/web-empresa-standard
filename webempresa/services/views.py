from django.shortcuts import render
from .models import Service

# Creamos la view de nuestros sevicios devolviendo la template correspondiente
def services(request):
    services = Service.objects.all() # aqui creamos una variable que almacena todos los objetos de la base de datos que pertenecen a services
    return render(request, "services/services.html", {'services':services})  # aqui pasamos la variable services para utilizar los valores en la template