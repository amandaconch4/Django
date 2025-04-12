from django import core
from django.shortcuts import render,redirect
from django.contrib import messages 
from .models import usuario,Perfil
from django.contrib.auth.decorators import login_required

# Create your views here.
def menu(request):
    return render(request, 'menuprincipal_wiki.html', {})

def foro(request):
    return render(request, 'forowiki.html', {})

def registro(request):
    return render(request, 'registrase_wiki.html', {})

def login(request):
    return render(request, 'inicio_sesion_wiki.html', {})

def cuenta(request):
    return render(request, 'micuentatf.html', {})

def animales(request):
    return render(request, 'Animales.html', {})

def mapa(request):
    return render(request, 'Lugarestf.html', {})

def enemigos(request):
    return render(request, 'Enemigos.html', {})

def construcciones(request):
    return render(request, 'Construcciones.html', {})

def plantas(request):
    return render(request, 'Flora.html', {})

def armas(request):
    return render(request, 'Armas.html', {})

def consumibles(request):
    return render(request, 'Consumibles.html', {})

def historia(request):
    return render(request, 'historia.html', {})

def recuperar(request):
    return render(request, 'recuperarcontra.html', {})

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registro')  # asegúrate de que este nombre coincida

        # Aquí guardamos el usuario en la base de datos Oracle
        try:
            # Verificar que el perfil "Usuario" exista, o crearlo
            perfil_usuario, creado = Perfil.objects.get_or_create(nombre_perfil='Usuario')

            nuevo_usuario = usuario(
                nombre_usuario=nombre,
                correo=email,
                contraseña=password,
                confir_contraseña=confirm_password,
                perfil=perfil_usuario
            )
            nuevo_usuario.save()
            messages.success(request, 'Usuario registrado correctamente.')
            return redirect('menu')

        except Exception as e:
            print("Error al registrar usuario:", e)
            messages.error(request, 'Error al registrar el usuario.')
            return redirect('registro')

    return redirect('registro')

def mi_cuenta(request):
    # Aquí puedes acceder a los datos del usuario autenticado
    usuario = request.user  # `request.user` es el usuario que está actualmente autenticado
    return render(request, 'micuentatf.html', {'usuario': usuario})
