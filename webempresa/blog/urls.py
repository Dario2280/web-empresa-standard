from django.urls import path
from . import views

# url de mis  vistas 
urlpatterns = [

    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category") #aqui hacemos pasar como cadena de caracteres con /<nombredelavariable>/
    
   
]
