# Modelos (tablas) de la app "pedidos" (Módulo 8: pedidos y reclamos derivados a Housekeeping o Mantenimiento, RF-38 a RF-41).
#
# Todavía NO hay modelos (Sprint 0). Entidades previstas:
#   - Pedido: pedido o reclamo de una unidad, área a la que se deriva (Housekeeping o Mantenimiento), estado y fechas.
#
# Recordatorio: nunca se borra un registro; se usa un campo
#   activo = models.BooleanField(default=True)
# y se hace "baja lógica" poniéndolo en False.

from django.db import models
