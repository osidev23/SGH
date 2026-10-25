# Pruebas de la app "portal". Se ejecutan con: python manage.py test portal

from django.test import TestCase
from django.urls import reverse


class IndexTests(TestCase):
    def test_responde_sin_iniciar_sesion(self):
        # El portal es público: cualquiera puede entrar
        respuesta = self.client.get(reverse('portal:index'))
        self.assertEqual(respuesta.status_code, 200)
