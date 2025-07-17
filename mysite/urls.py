from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('noti_blog.urls')),  # Incluye las URLs de tu app
]