from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return self.name

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)  
    contenido = models.TextField()
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.titulo