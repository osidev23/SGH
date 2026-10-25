# Vistas de la app "usuarios" (Módulo 1: usuarios, roles y login).
# Por ahora solo hay una página de inicio del módulo "En construcción".

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from usuarios.decorators import rol_requerido


@login_required
@rol_requerido()  # sin roles: solo entra el Gerente
def index(request):
    return render(request, 'usuarios/index.html')
