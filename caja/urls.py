# Rutas (URLs) de la app "caja". Se incluyen desde sgh/urls.py bajo /caja/.
# app_name permite nombrarlas como "caja:index" en templates y redirecciones.

from django.urls import path

from . import views

app_name = 'caja'

urlpatterns = [
    path('', views.index, name='index'),
]
