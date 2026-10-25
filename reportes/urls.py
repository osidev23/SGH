# Rutas (URLs) de la app "reportes". Se incluyen desde sgh/urls.py bajo /reportes/.
# app_name permite nombrarlas como "reportes:index" en templates y redirecciones.

from django.urls import path

from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.index, name='index'),
]
