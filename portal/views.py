# Vistas de la app "portal" (Módulo 5: portal público de reservas para huéspedes).
# Por ahora solo hay una página de inicio del módulo "En construcción".
# Este módulo es PÚBLICO: no lleva @login_required porque lo usan los huéspedes.

from django.shortcuts import render


def index(request):
    return render(request, 'portal/index.html')
