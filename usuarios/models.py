# Modelos de la app "usuarios" (Módulo 1: RF-01 a RF-04).
# Define el usuario del sistema con su rol, y la lista de módulos que puede ver cada rol.
# El Huésped NO es un usuario: entra al portal público con su código de reserva.

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Usuario interno del hotel. Hereda de AbstractUser todo lo de Django
    (username, password, nombre, apellido, email, is_active...) y le suma un rol."""

    class Rol(models.TextChoices):
        GERENTE = 'GERENTE', 'Gerente'
        RECEPCIONISTA = 'RECEPCIONISTA', 'Recepcionista'
        HOUSEKEEPING = 'HOUSEKEEPING', 'Housekeeping'
        MANTENIMIENTO = 'MANTENIMIENTO', 'Mantenimiento'

    rol = models.CharField('rol', max_length=20, choices=Rol.choices)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.get_full_name() or self.username

    def es_gerente(self):
        # El superusuario (creado con createsuperuser) también se considera Gerente.
        return self.rol == self.Rol.GERENTE or self.is_superuser

    def es_recepcionista(self):
        return self.rol == self.Rol.RECEPCIONISTA

    def es_housekeeping(self):
        return self.rol == self.Rol.HOUSEKEEPING

    def es_mantenimiento(self):
        return self.rol == self.Rol.MANTENIMIENTO

    def modulos_permitidos(self):
        """Devuelve los módulos de MODULOS que este usuario puede ver.
        Se usa en base.html (barra de navegación) e inicio.html (tarjetas)."""
        if self.es_gerente():
            return MODULOS
        return [modulo for modulo in MODULOS if self.rol in modulo['roles']]


# Módulos del sistema y qué roles (además del Gerente, que ve todo) pueden entrar.
# "url" es el nombre de la ruta de cada app (app_name:nombre).
# OJO: los roles de cada vista se controlan con @rol_requerido en su views.py;
# si cambian acá, hay que cambiarlos también allá.
MODULOS = [
    {
        'nombre': 'Usuarios',
        'url': 'usuarios:index',
        'descripcion': 'Alta de usuarios y asignación de roles.',
        'roles': [],
    },
    {
        'nombre': 'Unidades',
        'url': 'unidades:index',
        'descripcion': 'Habitaciones, departamentos, tarifas y tablero de estado.',
        'roles': [Usuario.Rol.RECEPCIONISTA, Usuario.Rol.HOUSEKEEPING, Usuario.Rol.MANTENIMIENTO],
    },
    {
        'nombre': 'Reservas',
        'url': 'reservas:index',
        'descripcion': 'Reservas internas y consulta de disponibilidad.',
        'roles': [Usuario.Rol.RECEPCIONISTA],
    },
    {
        'nombre': 'Huéspedes',
        'url': 'huespedes:index',
        'descripcion': 'Check-in, consumos y check-out.',
        'roles': [Usuario.Rol.RECEPCIONISTA],
    },
    {
        'nombre': 'Caja',
        'url': 'caja:index',
        'descripcion': 'Cobros, medios de pago, turnos y arqueo.',
        'roles': [Usuario.Rol.RECEPCIONISTA],
    },
    {
        'nombre': 'Pedidos',
        'url': 'pedidos:index',
        'descripcion': 'Pedidos y reclamos para Housekeeping y Mantenimiento.',
        'roles': [Usuario.Rol.RECEPCIONISTA, Usuario.Rol.HOUSEKEEPING, Usuario.Rol.MANTENIMIENTO],
    },
    {
        'nombre': 'Reportes',
        'url': 'reportes:index',
        'descripcion': 'Reportes de ocupación y caja para el Gerente.',
        'roles': [],
    },
    {
        'nombre': 'Portal público',
        'url': 'portal:index',
        'descripcion': 'Página de reservas que usan los huéspedes.',
        'roles': [Usuario.Rol.RECEPCIONISTA],
    },
]
