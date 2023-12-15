from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    descripcion = RichTextField(max_length=500)
    fecha_creacion = models.DateField()
    image = models.ImageField(upload_to='imagenes-blogs', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} - {self.autor}'
