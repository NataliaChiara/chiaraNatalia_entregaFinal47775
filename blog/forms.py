from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'autor', 'descripcion', 'fecha_creacion', 'image']
        widgets = {
            'descripcion': CKEditorWidget(),
        }