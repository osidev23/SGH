# Modelos (tablas) de la app "reportes" (Módulo 9: reportes para el Gerente, RF-42 a RF-45).
#
# Todavía NO hay modelos (Sprint 0). Entidades previstas:
#   - En principio ninguna propia: los reportes leen datos de las otras apps (ocupación, reservas, caja).
#
# Recordatorio: nunca se borra un registro; se usa un campo
#   activo = models.BooleanField(default=True)
# y se hace "baja lógica" poniéndolo en False.

from django.db import models
