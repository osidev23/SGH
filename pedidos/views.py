# Vistas de la app "pedidos" (Módulo 8: pedidos y reclamos derivados a Housekeeping o Mantenimiento).
# Por ahora solo hay una página de inicio del módulo "En construcción".

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from usuarios.decorators import rol_requerido
from usuarios.models import Usuario


@login_required
@rol_requerido(Usuario.Rol.RECEPCIONISTA, Usuario.Rol.HOUSEKEEPING, Usuario.Rol.MANTENIMIENTO)
def index(request):
    return render(request, 'pedidos/index.html')
