from django.urls import path
from . import views

# url de mis  vistas 
urlpatterns = [

    path('<int:page_id>/<slug:page_slug>/', views.page, name="page") #aqui hacemos pasar como cadena de caracteres con /<nombredelavariable>/
    
   
]
