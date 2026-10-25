# Modelos (tablas) de la app "huespedes" (Módulo 6: huéspedes, check-in, consumos y check-out, RF-25 a RF-32).
#
# Todavía NO hay modelos (Sprint 0). Entidades previstas:
#   - Huesped: nombre, documento, contacto.
#   - Estadia: check-in y check-out de una reserva, con sus huéspedes.
#   - Consumo: lo que el huésped consume durante la estadía (se cobra en el check-out).
#
# Recordatorio: nunca se borra un registro; se usa un campo
#   activo = models.BooleanField(default=True)
# y se hace "baja lógica" poniéndolo en False.

from django.db import models
