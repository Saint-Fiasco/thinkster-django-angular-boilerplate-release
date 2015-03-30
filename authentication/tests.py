from django.test import TestCase
from django.contrib.auth import login
from authentication.models import Usuario
# Create your tests here.

class CrearUsuarioTest(TestCase):
    def setUp(self):
        Usuario.objects.create_user('username', password='password', nombre='Juan', apellido='Perez', email='a@b.c')

    def getUserAttributes(self):
        usuario = Usuario.objects.get_by_natural_key('username')
        self.assertEqual(usuario.username, 'username')
        self.assertEqual(usuario.nombre, 'Juan')
        self.assertEqual(usuario.apellido, 'Perez')
        self.assertEqual(usuario.email, 'a@b.c')



