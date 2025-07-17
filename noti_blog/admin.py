from django.contrib import admin
from .models import Category, Noticia  # Asegúrate de importar tus modelos

admin.site.register(Category)  # Registra la tabla noti_blog_category
admin.site.register(Noticia)   # Registra la tabla noti_blog_noticia