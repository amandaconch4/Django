from django.urls import path
from .views import menu
from .views import foro
from .views import registro
from .views import login
from .views import cuenta
from .views import animales
from .views import mapa
from .views import enemigos
from .views import construcciones
from .views import plantas


urlpatterns = [
    path('menu', menu, name="menu"),
    path('menu/foro', foro, name="foro"),
    path('menu/registro', registro, name="registro"),
    path('menu/login', login, name="login"),
    path('menu/cuenta', cuenta, name="cuenta"),
    path('menu/animales', animales, name="animales"),
    path('menu/mapa', mapa, name="mapa"),
    path('menu/enemigos', enemigos, name="enemigos"),
    path('menu/construcciones', construcciones, name="construcciones"),
    path('menu/plantas', plantas, name="plantas")
]