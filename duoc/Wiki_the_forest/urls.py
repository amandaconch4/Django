from django.urls import path
from .views import menu
from .views import foro
from .views import registro
from .views import login


urlpatterns = [
    path('menu', menu, name="menu"),
    path('menu/foro', foro, name="foro"),
    path('menu/registro', registro, name="registro"),
    path('menu/login', login, name="login")
]