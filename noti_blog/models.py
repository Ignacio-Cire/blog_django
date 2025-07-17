from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Evita duplicados

    def __str__(self):
        return self.name

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Relación ForeignKey
    

    def __str__(self):
        return self.titulo