from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.lista_noticias, name='lista-noticias'),
     path('politica/', views.noticias_por_categoria, {'categoria': 'POLITICA'}, name='politica'),
    path('economia/', views.noticias_por_categoria, {'categoria': 'ECONOMIA'}, name='economia'),
    path('sociedad/', views.noticias_por_categoria, {'categoria': 'SOCIEDAD'}, name='sociedad'),
    path('espectaculos/', views.noticias_por_categoria, {'categoria': 'ESPECTACULOS'}, name='espectaculos'), 
    path('deportes/', views.noticias_por_categoria, name='deportes'), 
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)