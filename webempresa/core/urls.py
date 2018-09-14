from django.urls import path
from . import views

# url de mis  vistas 
urlpatterns = [

    path('', views.home, name="home"),
    
    path('store/', views.store, name="store"),
   


    
   
]
