# Modelos (tablas) de la app "unidades" (Módulos 2 y 3: habitaciones, departamentos, tarifas, promociones y tablero de estado, RF-05 a RF-14).
#
# Todavía NO hay modelos (Sprint 0). Entidades previstas:
#   - TipoUnidad: habitación o departamento (23 habitaciones y 11 departamentos).
#   - Unidad: número, tipo, capacidad, estado (libre, ocupada, limpieza, mantenimiento) y fotos.
#   - Tarifa: precio por noche según tipo de unidad y temporada.
#   - Promocion: descuentos por fechas o cantidad de noches.
#
# Recordatorio: nunca se borra un registro; se usa un campo
#   activo = models.BooleanField(default=True)
# y se hace "baja lógica" poniéndolo en False.

from django.db import models
