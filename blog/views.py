from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from blog.models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BlogForm

class ListadoBlogs(ListView):
    model = Blog
    context_object_name = 'listado_de_blogs'
    template_name = 'blog/blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs_con_imagen'] = Blog.objects.exclude(image__isnull=True)
        return context


class CrearBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/crear_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('blogs')

class ActualizarBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog/actualizar_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('blogs')

class DetalleBlog(DetailView):
    model = Blog
    template_name = 'blog/detalle_blog.html'

class EliminarBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/eliminar_blog.html'
    success_url = reverse_lazy('blogs')