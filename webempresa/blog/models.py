from django.db import models # importacion predertminada por django
from django.utils.timezone import now #importamos la funcion now() para registar el momento exacto de la publicacion de nuestro post
from django.contrib.auth.models import User #importamos la model User para poder relacionarla al autor de las publicaciones del post

# creamos nuestras models aqui 

#aqui creamos la clase Category para nuestra model de categoria
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="categoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion") #aqui registramos el momento de creacion de la categoria
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de actualizacion") #aqui registramos la ultima actualizacion de la categoria respectiva

    class Meta:  #generamos una clase Meta para poder traducir correctamente como deseamos el titulo de nuestra model en el panel adminstrativo
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created'] #revertimos nuestra lista para asi poder ir imprimiendo en pantalla las ultimas

    def __str__(self):
        return self.name #aqui utilizamos un metodo para poder mandar el nombre de la categoria




#aqui creamos la clase Post para nuestra model de Post
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    content = models.TextField(verbose_name="contenido")
    published = models.DateTimeField(verbose_name="fecha de publicacion", default=now()) #utilizamos la funcion now() importada de django.utils.timezone
    image = models.ImageField(verbose_name="imagen", upload_to="blog", blank=True, null=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name='author_post') #utilizamos el ForeignKey para relacionar con la llave forania nuestro User (usuario) como author
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts") #utilizamos ManytoManyField para relacionar de todos a todos nuestra categoria y utilizamos get_posts para utilizarlo en nuestra template 
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion") #aqui registramos la creacion del post o la publicacion respectiva
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de actualizacion") #aqui registramos la ultima actualizacion del post o publicacion respectiva

    class Meta: #generamos una clase Meta para poder traducir correctamente como deseamos el titulo de nuestra model en el panel adminstrativo
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created'] #revertimos nuestra lista para asi poder ir imprimiendo en pantalla las ultimas

    def __str__(self):
        return self.title  #aqui utilizamos un metodo para poder mandar el nombre del Post

