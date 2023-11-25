from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from automovil.models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListadoAutomoviles(ListView):
    model = Blog
    context_object_name = 'listado_de_blogs'
    template_name = 'blog/blogs.html'

class CrearAutomovil(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/crear_blog.html'
    fields= ['titulo', 'autor', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('automoviles')

class ActualizarAutomovil(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog/actualizar_blog.html'
    fields= ['titulo', 'autor', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('automoviles')

class DetalleAutomovil(DetailView):
    model = Blog
    template_name = 'blog/detalle_blog.html'

class EliminarAutomovil(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/eliminar_blog.html'
    success_url = reverse_lazy('automoviles')