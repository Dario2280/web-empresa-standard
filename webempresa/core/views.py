from django.shortcuts import render

# mis vistas con sus respectivos templates a seren solicitados
def home(request):
    return render(request, "core/home.html")




def store(request):
    return render(request, "core/store.html") 



