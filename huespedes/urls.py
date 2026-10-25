# Rutas (URLs) de la app "huespedes". Se incluyen desde sgh/urls.py bajo /huespedes/.
# app_name permite nombrarlas como "huespedes:index" en templates y redirecciones.

from django.urls import path

from . import views

app_name = 'huespedes'

urlpatterns = [
    path('', views.index, name='index'),
]
