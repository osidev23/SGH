# Vistas generales del proyecto (las que no pertenecen a ningún módulo).

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def inicio(request):
    # Página principal después del login. Las tarjetas de cada módulo
    # se arman en inicio.html con user.modulos_permitidos.
    return render(request, 'inicio.html')
