from django.urls import path
from blog.views import ListadoBlogs, CrearBlog, ActualizarBlog, EliminarBlog, DetalleBlog

urlpatterns = [
    path('blogs/', ListadoBlogs.as_view(), name='blogs'),
    path('blogs/crear', CrearBlog.as_view(), name='crear_blog'),
    path('blogs/<int:pk>', DetalleBlog.as_view(), name='detalle_blog'),
    path('blogs/<int:pk>/eliminar', EliminarBlog.as_view(), name='eliminar_blog'),
    path('blogs/<int:pk>/actualizar', ActualizarBlog.as_view(), name='actualizar_blog')
]