from django.urls import path
from .views import menu
from .views import foro
from .views import registro
from .views import login
from .views import animales
from .views import mapa
from .views import enemigos
from .views import construcciones
from .views import plantas
from .views import armas
from .views import consumibles
from .views import historia
from .views import recuperar
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('menu', menu, name="menu"),
    path('menu/foro', foro, name="foro"),
    path('menu/registro', registro, name="registro"),
    path('menu/login', views.iniciar_sesion, name="login"),
    path('menu/animales', animales, name="animales"),
    path('menu/mapa', mapa, name="mapa"),
    path('menu/enemigos', enemigos, name="enemigos"),
    path('menu/construcciones', construcciones, name="construcciones"),
    path('menu/plantas', plantas, name="plantas"),
    path('menu/armas', armas, name="armas"),
    path('menu/consumibles', consumibles, name="consumibles"),
    path('menu/historia', historia, name="historia"),
    path('menu/recuperar', recuperar, name="recuperar"),
    path('menu/registro_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('mi-cuenta/', views.mi_cuenta, name='mi_cuenta'),
    path('editar-cuenta/', views.editar_cuenta, name='editar_cuenta'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('login/', views.iniciar_sesion, name='login'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('registro/', views.registro, name='registro'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)