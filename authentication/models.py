from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    '''
       @cvar UsuarioManager: controlador de la clase B{Usuario}
       @param nombre de usuario
    '''
    def create_user(self, username, password=None, **kwargs):
        '''
        :param username: nombre del usuario del sistema
        @type username: string de 40 caracteres
        :param password: contrasenha del usuario
        @type password: string heredado del framework
        :param kwargs: otros datos
        :return: usuario
        '''
        if not username:
            raise ValueError('Debe existir un nombre de usuario')

        if not kwargs.get('email'):
            raise ValueError('Debe tener una direccion de correo valida')

        if not kwargs.get('nombre'):
            raise ValueError('El usuario debe tener un nombre')

        if not kwargs.get('apellido'):
            raise ValueError('El usuario debe tener un apellido')

        usuario = self.model(
            username=username,
            email=self.normalize_email(kwargs.get('email')),
            nombre=kwargs.get('nombre'),
            apellido=kwargs.get('apellido')
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, password=None, **kwargs):
        '''
        funcion B{crear superusuario} funcion para crear un superusuario
        @param username:: nombre del usuario del sistema
        @type username: string de 40 caracteres
        @param password: contrasenha del usuario
        @type password: string agregado por el framework
        @param kwargs: otros datos
        '''
        usuario = self.create_user(username, password, **kwargs)
        usuario.is_admin = True
        usuario.save()
        return usuario

    def crear_cliente(self, username, password=None, **kwargs):
        '''
        funcion B{crear cliente} funcion que crea usuarios de tipo cliente
        @param username:: nombre del usuario del sistema
        @type username: string de 40 caracteres
        @param password: contrasenha del usuario
        @type password: string agregado por el framework
        @param kwargs: otros datos
        '''
        usuario = self.create_user(username, password, **kwargs)
        usuario.tipo='CLIENTE'
        usuario.save()
        return usuario

    def crear_empleado(self, username, password=None, **kwargs):
        '''
        funcion B{crear empleado} funcion que crea usuarios de tipo empleado
        @param username:: nombre del usuario del sistema
        @type username: string de 40 caracteres
        @param password: contrasenha del usuario
        @type password: string agregado por el framework
        @param kwargs: otros datos
        '''
        usuario = self.create_user(username, password, **kwargs)
        usuario.tipo='EMPLEADO'
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    '''
    @cvar Usuario: con I{nombre}, I{apellido}, I{email}, I{telefono}, I{direccion}, I{tipo de usuario} y I{estado}
    I{email}, I{nombre} y I{apellido}
    I{nombre},I{apellido}: para I{get_nombre_completo}
    '''
    username = models.CharField(max_length=40, unique=True)

    nombre = models.CharField(max_length=40, blank=True)
    apellido = models.CharField(max_length=40, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=50, blank=True)

    tipo = models.CharField(max_length=23)

    activo = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']
    def __unicode__(self):
        return self.username

    def get_nombre_completo(self):
        return ''.join([self.nombre, self.apellido])

    def get_nombre(self):
        return self.nombre


