from django.urls import path
from . import views

# url de mis  vistas 
urlpatterns = [

    path('', views.contact, name="contact"),
      
]
