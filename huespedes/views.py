# Vistas de la app "huespedes" (Módulo 6: huéspedes, check-in, consumos y check-out).
# Por ahora solo hay una página de inicio del módulo "En construcción".

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from usuarios.decorators import rol_requerido
from usuarios.models import Usuario


@login_required
@rol_requerido(Usuario.Rol.RECEPCIONISTA)
def index(request):
    return render(request, 'huespedes/index.html')
