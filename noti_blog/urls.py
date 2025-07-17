from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_noticias, name='lista-noticias'),
     path('politica/', views.noticias_por_categoria, {'categoria': 'POLITICA'}, name='politica'),
    path('economia/', views.noticias_por_categoria, {'categoria': 'ECONOMIA'}, name='economia'),
    path('sociedad/', views.noticias_por_categoria, {'categoria': 'SOCIEDAD'}, name='sociedad'),
    path('deportes/', views.noticias_por_categoria, {'categoria': 'DEPORTES'}, name='deportes'),
    path('espectaculos/', views.noticias_por_categoria, {'categoria': 'ESPECTACULOS'}, name='espectaculos'),    
    

]