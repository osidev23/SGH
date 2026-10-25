# Rutas (URLs) de la app "reservas". Se incluyen desde sgh/urls.py bajo /reservas/.
# app_name permite nombrarlas como "reservas:index" en templates y redirecciones.

from django.urls import path

from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.index, name='index'),
]
