from django.urls import path
from .views import menu
from .views import foro
from .views import registro
from .views import login
from .views import cuenta
from .views import animales


urlpatterns = [
    path('menu', menu, name="menu"),
    path('menu/foro', foro, name="foro"),
    path('menu/registro', registro, name="registro"),
    path('menu/login', login, name="login"),
    path('menu/cuenta', cuenta, name="cuenta"),
    path('menu/animales', animales, name="animales")
]