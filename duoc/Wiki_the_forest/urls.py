from django.urls import path
from .views import menu
from .views import foro


urlpatterns = [
    path('menu', menu, name="menu"),
    path('menu/foro', foro, name="foro"),
]