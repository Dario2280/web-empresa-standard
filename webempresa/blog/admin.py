from django.contrib import admin
from .models import Category, Post
# Register your models here.

#aqui creamos la configuraciones e nuestra CATEGORIA para añadirla al admin
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #esta clase crea la configuracion de mi categoria dejando la hora y fehca de modificacion y piblicacion solo para lectura

#aqui creamos la configuraciones e nuestra POST para añadirla al admin

#aqui reside las configuraciones de como recibimos los datos en el admin referente a este model
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author','published', 'post_categories') #Con esta opcion podemos crear una lista pasando los parametros de los datos que queremos ver
    ordering = ('author', 'published') # ordenamos segun queramos la listas
    search_fields = ('title', 'content', 'author__username', 'categories__name') #aqui creamos un buscador para nuestros post en el admin
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")]) #aqui solicitamos un for en todas las cateorias para poder mostrarla en la lista

    post_categories.short_description = "categorias" #aqui cambiamos el nombre de la variable "post_categories" por "categorias"

#añadimos al admin nuestras models Category y Post
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)