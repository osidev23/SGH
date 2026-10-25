# Pruebas de la app "reservas". Se ejecutan con: python manage.py test reservas

from django.test import TestCase
from django.urls import reverse

from usuarios.models import Usuario


class IndexTests(TestCase):
    def test_responde_con_rol_correcto(self):
        usuario = Usuario.objects.create_user(
            username='prueba', password='clave-de-prueba', rol=Usuario.Rol.RECEPCIONISTA
        )
        self.client.force_login(usuario)
        respuesta = self.client.get(reverse('reservas:index'))
        self.assertEqual(respuesta.status_code, 200)
