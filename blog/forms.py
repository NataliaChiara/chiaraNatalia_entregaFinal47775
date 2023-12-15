from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'autor', 'descripcion', 'fecha_creacion', 'image']
