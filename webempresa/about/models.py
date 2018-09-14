from django.db import models # importacion predertminada por django
from django.contrib.auth.models import User #importamos la model User para poder relacionarla al autor de las publicaciones del post

# creamos nuestras models aqui 





#aqui creamos la clase About para nuestra model de About
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    subtitle = models.CharField(max_length=200, verbose_name="subtitulo")
    content = models.TextField(verbose_name="contenido")
    image = models.ImageField(verbose_name="imagen", upload_to="about")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name='author_about') #utilizamos el ForeignKey para relacionar con la llave forania nuestro User (usuario) como author
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion") #aqui registramos la creacion del post o la publicacion respectiva
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de actualizacion") #aqui registramos la ultima actualizacion del post o publicacion respectiva
    order = models.SmallIntegerField(verbose_name="Orden", default=0) #el orden de nuestras historias

    class Meta: #generamos una clase Meta para poder traducir correctamente como deseamos el titulo de nuestra model en el panel adminstrativo
        verbose_name = "historia"
        verbose_name_plural = "historias"
        ordering = ['order', 'title'] #revertimos nuestra lista para asi poder ir imprimiendo en pantalla las ultimas

    def __str__(self):
        return self.title  #aqui utilizamos un metodo para poder mandar el nombre del About

