# Modelos (tablas) de la app "caja" (Módulo 7: cobros, medios de pago, apertura/cierre de turno y arqueo, RF-33 a RF-37).
#
# Todavía NO hay modelos (Sprint 0). Entidades previstas:
#   - Cobro: monto, fecha, medio de pago y a qué estadía o reserva corresponde.
#   - MedioPago: efectivo, transferencia, posnet.
#   - TurnoCaja: apertura, cierre y arqueo de cada turno.
#
# Fuera de alcance: facturación electrónica y funciones fiscales (ARCA/AFIP).
# Solo se registran cobros y medios de pago.
#
# Recordatorio: nunca se borra un registro; se usa un campo
#   activo = models.BooleanField(default=True)
# y se hace "baja lógica" poniéndolo en False.

from django.db import models
