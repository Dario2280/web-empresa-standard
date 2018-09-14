from django.contrib import admin
from .models import Service #Importamos la model Service que es de la seccion de servicios

# registramos nuesta model aqui dentro del panel administrativo
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #aqui convertimos los valores de captura de fecha como solo lectura

admin.site.register(Service, ServiceAdmin)    #aqui registramos en el admin nuestras models
