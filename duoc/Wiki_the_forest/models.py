from django.db import models

# Create your models here.
class Perfil(models.Model):
    nombre_perfil = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_perfil
    
class usuario (models.Model):
    nombre_usuario = models.CharField(max_length=200, unique=True)
    correo = models.CharField(max_length=200, unique=True)
    contraseña = models.CharField(max_length=200)
    confir_contraseña = models.CharField(max_length=200)
    foto = models.ImageField(upload_to= 'usuarios/', null = True, blank=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='usuarios')

    def __str__(self):
        return self.get_name_profile()

    def get_name_profile(self):
        return f" {self.nombre_usuario} - Perfil: {self.perfil.nombre_perfil}"

