from django import core
from django.shortcuts import render,redirect
from django.contrib import messages 
from .models import usuario,Perfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def menu(request):
    return render(request, 'menuprincipal_wiki.html', {})

def foro(request):
    return render(request, 'forowiki.html', {})

def registro(request):
    return render(request, 'registrase_wiki.html', {})

def login(request):
    return render(request, 'inicio_sesion_wiki.html', {})

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
            return redirect('registro') 

        # Aquí guardamos el usuario en la base de datos
        try:
            # Verificar que el usuario exista o crearlo
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
            return redirect('login')

        except Exception as e:
            print("Error al registrar usuario:", e)
            messages.error(request, 'Error al registrar el usuario.')
            return redirect('registro')

    return redirect('registro')

def iniciar_sesion(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        password = request.POST.get('password')
        
        try:
            # Verificar si existe el usuario
            user_custom = usuario.objects.get(nombre_usuario=nombre_usuario, contraseña=password)
            
            # Crear o actualizar el usuario
            user, created = User.objects.get_or_create(username=nombre_usuario)
            if created:
                user.set_password(password)
                user.save()
            
            # Autenticar y logear al usuario
            auth_login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('mi_cuenta')
            
        except usuario.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect('login')
    
    return render(request, 'inicio_sesion_wiki.html')

def cerrar_sesion(request):
    auth_logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('menu')

@login_required(login_url='login')
def mi_cuenta(request):
    try:
        user = usuario.objects.get(nombre_usuario=request.user.username)
        return render(request, 'micuentatf.html', {'usuario': user})
    except usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('login')

@login_required(login_url='login')
def editar_cuenta(request):
    if request.method == 'POST':
        try:
            user = usuario.objects.get(nombre_usuario=request.user.username)
            
            # Actualizar los campos
            nuevo_nombre = request.POST.get('nombre')
            nuevo_email = request.POST.get('email')
            nueva_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            nueva_foto = request.FILES.get('foto')
            
            if nueva_password:
                if nueva_password != confirm_password:
                    messages.error(request, 'Las contraseñas no coinciden.')
                    return redirect('mi_cuenta')
                user.contraseña = nueva_password
                user.confir_contraseña = confirm_password
                
                # Actualizar también la contraseña del usuario
                django_user = User.objects.get(username=request.user.username)
                django_user.set_password(nueva_password)
                django_user.save()
            
            if nuevo_nombre:
                user.nombre_usuario = nuevo_nombre
                # Actualizar también el nombre de usuario
                django_user = User.objects.get(username=request.user.username)
                django_user.username = nuevo_nombre
                django_user.save()
                
            if nuevo_email:
                user.correo = nuevo_email
                
            if nueva_foto:
                user.foto = nueva_foto
                
            user.save()
            messages.success(request, 'Datos actualizados correctamente.')
            
            # Si se cambió la contraseña, hacer logout para que el usuario vuelva a iniciar sesión
            if nueva_password:
                return redirect('login')
            return redirect('mi_cuenta')
            
        except usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
            return redirect('login')
            
    return redirect('mi_cuenta')
