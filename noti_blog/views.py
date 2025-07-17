from django.shortcuts import render, redirect  # Añade 'redirect'
from .models import Noticia, Category 
from django.shortcuts import render, get_object_or_404
from .models import Noticia
from .forms import NoticiaForm  # Asegúrate de tener forms.py (paso siguiente)

def lista_noticias(request):
    # Si el usuario envía datos (POST)
    if request.method == 'POST':
        form = NoticiaForm(request.POST)  # Crea el formulario con los datos recibidos
        if form.is_valid():
            form.save()  # Guarda en la BD
            return redirect('lista-noticias')  # Recarga la página
    
    # Si el usuario solo ve la página (GET)
    else:
        form = NoticiaForm()  # Formulario vacío
    
    noticias = Noticia.objects.all()  # Obtiene todas las noticias
    
    return render(request, 'noti_blog/lista_noticias.html', {
        'noticias': noticias,
        'form': form  # Pasa el formulario al template
    })


def noticias_por_categoria(request):
    categoria = get_object_or_404(Category, name='DEPORTES')
    noticias = Noticia.objects.filter(categoria=categoria)  # Filtra por objeto
    return render(request, 'noti_blog/deportes.html', {'noticias': noticias})

def deportes(request):
    categoria_deportes = Category.objects.get(name='DEPORTES')
    noticias_deportes = Noticia.objects.filter(categoria=categoria_deportes)
    return render(request, 'noti_blog/deportes.html', {
        'noticias': noticias_deportes,
        'categoria': categoria_deportes
    })