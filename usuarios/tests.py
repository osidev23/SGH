# Pruebas de la app "usuarios": roles, login y permisos.
# Se ejecutan con: python manage.py test usuarios

from django.test import TestCase
from django.urls import reverse

from .models import Usuario


class UsuarioTests(TestCase):
    def test_metodos_de_rol(self):
        recepcionista = Usuario(username='ana', rol=Usuario.Rol.RECEPCIONISTA)
        self.assertTrue(recepcionista.es_recepcionista())
        self.assertFalse(recepcionista.es_gerente())

    def test_superusuario_es_gerente(self):
        admin = Usuario(username='admin', is_superuser=True)
        self.assertTrue(admin.es_gerente())


class AccesoTests(TestCase):
    def test_pagina_de_login_responde(self):
        respuesta = self.client.get(reverse('login'))
        self.assertEqual(respuesta.status_code, 200)

    def test_inicio_sin_sesion_redirige_al_login(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertRedirects(respuesta, reverse('login') + '?next=/')

    def test_inicio_muestra_solo_modulos_del_rol(self):
        recepcionista = Usuario.objects.create_user(
            username='ana', password='clave-de-prueba', rol=Usuario.Rol.RECEPCIONISTA
        )
        self.client.force_login(recepcionista)
        respuesta = self.client.get(reverse('inicio'))
        self.assertContains(respuesta, 'Reservas')
        self.assertNotContains(respuesta, 'Reportes')

    def test_index_responde_al_gerente(self):
        gerente = Usuario.objects.create_user(
            username='gerente', password='clave-de-prueba', rol=Usuario.Rol.GERENTE
        )
        self.client.force_login(gerente)
        respuesta = self.client.get(reverse('usuarios:index'))
        self.assertEqual(respuesta.status_code, 200)

    def test_rol_sin_permiso_recibe_403(self):
        mucama = Usuario.objects.create_user(
            username='mucama', password='clave-de-prueba', rol=Usuario.Rol.HOUSEKEEPING
        )
        self.client.force_login(mucama)
        respuesta = self.client.get(reverse('usuarios:index'))
        self.assertEqual(respuesta.status_code, 403)
