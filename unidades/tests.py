# Pruebas de la app "unidades". Se ejecutan con: python manage.py test unidades

from django.test import TestCase
from django.urls import reverse

from usuarios.models import Usuario


class IndexTests(TestCase):
    def test_responde_con_rol_correcto(self):
        usuario = Usuario.objects.create_user(
            username='prueba', password='clave-de-prueba', rol=Usuario.Rol.HOUSEKEEPING
        )
        self.client.force_login(usuario)
        respuesta = self.client.get(reverse('unidades:index'))
        self.assertEqual(respuesta.status_code, 200)
