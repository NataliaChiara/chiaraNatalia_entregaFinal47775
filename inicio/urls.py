
from django.urls import path
from inicio.views import inicio, acerca

urlpatterns = [
    path('', inicio, name='inicio'),
    path('acerca/', acerca, name='acerca')
]
