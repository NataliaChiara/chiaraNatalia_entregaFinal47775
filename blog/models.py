from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo= models.CharField(max_length=30)
    autor= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=500)
    fecha_creacion= models.DateField()
    image = models.ImageField(upload_to='imagenes-blogs', null=True, blank=True)


    def __str__(self):
        return f'{self.titulo} - {self.autor}'