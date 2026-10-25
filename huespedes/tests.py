# Pruebas de la app "huespedes". Se ejecutan con: python manage.py test huespedes

from django.test import TestCase
from django.urls import reverse

from usuarios.models import Usuario


class IndexTests(TestCase):
    def test_responde_con_rol_correcto(self):
        usuario = Usuario.objects.create_user(
            username='prueba', password='clave-de-prueba', rol=Usuario.Rol.RECEPCIONISTA
        )
        self.client.force_login(usuario)
        respuesta = self.client.get(reverse('huespedes:index'))
        self.assertEqual(respuesta.status_code, 200)
