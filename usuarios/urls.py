# Rutas (URLs) de la app "usuarios". Se incluyen desde sgh/urls.py bajo /usuarios/.
# app_name permite nombrarlas como "usuarios:index" en templates y redirecciones.

from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.index, name='index'),
]
