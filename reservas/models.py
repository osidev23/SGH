# Modelos (tablas) de la app "reservas" (Módulo 4: reservas internas y disponibilidad, RF-15 a RF-19).
#
# Todavía NO hay modelos (Sprint 0). Entidades previstas:
#   - Reserva: unidad, fechas de entrada y salida, datos de contacto, estado y código de reserva.
#
# Recordatorio: nunca se borra un registro; se usa un campo
#   activo = models.BooleanField(default=True)
# y se hace "baja lógica" poniéndolo en False.

from django.db import models
