# Modelos (tablas) de la app "portal" (Módulo 5: portal público de reservas para huéspedes, RF-20 a RF-24).
#
# Todavía NO hay modelos (Sprint 0). Entidades previstas:
#   - En principio ninguna propia: el portal usa Reserva (app reservas) y Unidad (app unidades).
#   - El huésped no tiene usuario: consulta su reserva con el código de reserva.
#
# Recordatorio: nunca se borra un registro; se usa un campo
#   activo = models.BooleanField(default=True)
# y se hace "baja lógica" poniéndolo en False.

from django.db import models
