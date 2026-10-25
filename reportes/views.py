# Vistas de la app "reportes" (Módulo 9: reportes para el Gerente).
# Por ahora solo hay una página de inicio del módulo "En construcción".

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from usuarios.decorators import rol_requerido


@login_required
@rol_requerido()  # sin roles: solo entra el Gerente
def index(request):
    return render(request, 'reportes/index.html')
