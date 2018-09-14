from django.contrib import admin
from .models import About
# Register your models here.



#aqui creamos la configuraciones e nuestra About para añadirla al admin

#aqui reside las configuraciones de como recibimos los datos en el admin referente a este model
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author') #Con esta opcion podemos crear una lista pasando los parametros de los datos que queremos ver
    ordering = ('author',) # ordenamos segun queramos la listas



    

    

#añadimos al admin nuestras models Category y Post

admin.site.register(About, AboutAdmin)