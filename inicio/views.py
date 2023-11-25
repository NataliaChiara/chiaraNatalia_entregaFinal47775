from django.shortcuts import render, redirect
from inicio.models import Paleta
from inicio.forms import CrearPaletaFormulario, BusquedaPaletaFormulario, ActualizarPaletaFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def paletas(request):
    formulario = BusquedaPaletaFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_paletas = Paleta.objects.filter(marca__icontains = marca_a_buscar)

    formulario = BusquedaPaletaFormulario()
    return render(request, 'inicio/paletas.html', {'formulario': formulario, 'listado_de_paletas': listado_de_paletas}) 
    
@login_required
def crear_paleta(request):
    if request.method == 'POST':
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            paleta = Paleta(marca=marca.lower(), descripcion=descripcion, anio=anio)
            paleta.save() #esto lo guarda en la base de datos cuando se accede a la pagina '/paletas/crear'
            return redirect('paletas')
        else:
            return render(request, 'inicio/crear_paleta.html' , {'formulario': formulario})

    formulario = CrearPaletaFormulario()
    return render(request, 'inicio/crear_paleta.html' , {'formulario': formulario})

@login_required
def eliminar_paleta (request, paleta_id):
    paleta_a_eliminar = Paleta.objects.get(id=paleta_id) # OJO CON EL GET, PUEDE ROMPER
    paleta_a_eliminar.delete()
    return redirect('paletas')

@login_required
def actualizar_paleta (request, paleta_id):
    paleta_a_actualizar = Paleta.objects.get(id=paleta_id)
    if request.method == 'POST':
        formulario = ActualizarPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            paleta_a_actualizar.marca = info_nueva.get('marca')
            paleta_a_actualizar.descripcion = info_nueva.get('descripcion')
            paleta_a_actualizar.anio = info_nueva.get('anio')
            paleta_a_actualizar.save()
            return redirect('paletas')
        else:
            return render(request, 'inicio/actualizar_paleta.html', {'formulario': formulario})

    formulario = ActualizarPaletaFormulario(initial={'marca': paleta_a_actualizar.marca, 'descripcion': paleta_a_actualizar.descripcion, 'anio': paleta_a_actualizar.anio})
    return render(request, 'inicio/actualizar_paleta.html', {'formulario': formulario})

def detalle_paleta(request, paleta_id):
    paleta = Paleta.objects.get(id=paleta_id)
    return render(request, 'inicio/detalle_paleta.html', {'paleta': paleta})