# Decorador para restringir una vista según el rol del usuario.
#
# Uso (siempre debajo de @login_required, para que primero pida iniciar sesión):
#
#     @login_required
#     @rol_requerido(Usuario.Rol.RECEPCIONISTA)
#     def mi_vista(request):
#         ...
#
# El Gerente pasa siempre. El resto solo si su rol está en la lista.
# Si no tiene permiso, Django muestra un error 403 (Prohibido).

from functools import wraps

from django.core.exceptions import PermissionDenied


def rol_requerido(*roles):
    def decorador(vista):
        @wraps(vista)
        def envoltura(request, *args, **kwargs):
            usuario = request.user
            if usuario.es_gerente() or usuario.rol in roles:
                return vista(request, *args, **kwargs)
            raise PermissionDenied
        return envoltura
    return decorador
