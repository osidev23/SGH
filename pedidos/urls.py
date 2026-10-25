# Rutas (URLs) de la app "pedidos". Se incluyen desde sgh/urls.py bajo /pedidos/.
# app_name permite nombrarlas como "pedidos:index" en templates y redirecciones.

from django.urls import path

from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.index, name='index'),
]
