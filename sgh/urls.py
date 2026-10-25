"""
Rutas (URLs) principales del proyecto SGH.

Cada línea de urlpatterns conecta una dirección del navegador con una vista.
Las rutas de cada módulo están en el urls.py de su app y se "enchufan" acá con include().

Documentación: https://docs.djangoproject.com/es/5.2/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # Login y logout con las vistas que ya trae Django (template: templates/registration/login.html)
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Página de inicio (tarjetas con los módulos del usuario)
    path('', views.inicio, name='inicio'),

    # Un include por app (módulo)
    path('usuarios/', include('usuarios.urls')),
    path('unidades/', include('unidades.urls')),
    path('reservas/', include('reservas.urls')),
    path('portal/', include('portal.urls')),
    path('huespedes/', include('huespedes.urls')),
    path('caja/', include('caja.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('reportes/', include('reportes.urls')),
]

# En desarrollo (DEBUG=True), Django sirve también los archivos subidos a media/.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
