# Rutas (URLs) de la app "unidades". Se incluyen desde sgh/urls.py bajo /unidades/.
# app_name permite nombrarlas como "unidades:index" en templates y redirecciones.

from django.urls import path

from . import views

app_name = 'unidades'

urlpatterns = [
    path('', views.index, name='index'),
]
