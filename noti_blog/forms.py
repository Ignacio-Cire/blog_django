from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido']  # Campos que se mostrarán en el formulario