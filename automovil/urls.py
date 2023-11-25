from django.urls import path
from automovil.views import ListadoBlogs, CrearBlog, ActualizarBlog, EliminarBlog, DetalleBlog

urlpatterns = [
    path('automoviles/', ListadoBlogs.as_view(), name='blogs'),
    path('automoviles/crear', CrearBlog.as_view(), name='crear_blog'),
    path('automoviles/<int:pk>', DetalleBlog.as_view(), name='detalle_blog'),
    path('automoviles/<int:pk>/eliminar', EliminarBlog.as_view(), name='eliminar_blog'),
    path('automoviles/<int:pk>/actualizar', ActualizarBlog.as_view(), name='actualizar_blog')
]