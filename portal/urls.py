# Rutas (URLs) de la app "portal". Se incluyen desde sgh/urls.py bajo /portal/.
# app_name permite nombrarlas como "portal:index" en templates y redirecciones.

from django.urls import path

from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.index, name='index'),
]
