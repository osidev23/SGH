# Registra el modelo Usuario en el panel de administración de Django (/admin/).
# Usamos UserAdmin (el que trae Django para usuarios) y le agregamos el campo "rol".

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Columnas y filtros del listado de usuarios
    list_display = ('username', 'first_name', 'last_name', 'rol', 'is_active')
    list_filter = ('rol', 'is_active', 'is_staff')

    # Formulario para editar un usuario: los campos de siempre + el rol
    fieldsets = UserAdmin.fieldsets + (
        ('Rol en el hotel', {'fields': ('rol',)}),
    )

    # Formulario para crear un usuario nuevo: también pide el rol
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol en el hotel', {'fields': ('first_name', 'last_name', 'rol')}),
    )
