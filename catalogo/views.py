from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegistroUsuarioForm, EditarPerfilForm, LibroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Libro
from django.contrib.auth import logout

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Usuario registrado con éxito!")
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'catalogo/registro.html', {'form': form})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'catalogo/editar_perfil.html', {'form': form})

def registrar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.usuario = request.user
            libro.save()
            return redirect('perfil')  
    else:
        form = LibroForm()
    return render(request, 'catalogo/registrar_libro.html', {'form': form})

def perfil_usuario(request):
    libros = Libro.objects.filter(usuario=request.user)
    return render(request, 'catalogo/perfil.html', {
        'user': request.user,
        'libros': libros
    })

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id, usuario=request.user)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'catalogo/editar_libro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('catalogo:login')  

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id, usuario=request.user)
    
    if request.method == 'POST':
        libro.delete()
        return redirect('perfil')

    return render(request, 'catalogo/eliminar_libro.html', {'libro': libro})
