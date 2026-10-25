"""
Configuración general del proyecto SGH (Sistema de Gestión Hotelera).

Acá se define todo lo que Django necesita saber para funcionar: qué apps
usa, a qué base de datos se conecta, en qué idioma y zona horaria trabaja,
dónde están los templates y archivos estáticos, etc.

Los datos sensibles (clave secreta, contraseña de la base) NO se escriben
acá: se leen del archivo .env (ver .env.example).

Documentación: https://docs.djangoproject.com/es/5.2/ref/settings/
"""

import os
from pathlib import Path

from django.contrib import messages
from dotenv import load_dotenv

# Carpeta raíz del proyecto (donde está manage.py). Se usa para armar rutas: BASE_DIR / 'templates'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Lee el archivo .env y carga sus valores como variables de entorno.
load_dotenv(BASE_DIR / '.env')


# Seguridad: clave secreta, modo debug y dominios permitidos (todo viene del .env).
# DEBUG en True muestra errores detallados; en producción tiene que ir en False.
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


# Apps instaladas: las de Django (arriba) y las nuestras, una por módulo (abajo).
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps del SGH
    'usuarios',   # Módulo 1: usuarios, roles y login
    'unidades',   # Módulos 2 y 3: habitaciones, departamentos, tarifas y tablero
    'reservas',   # Módulo 4: reservas internas
    'portal',     # Módulo 5: portal público de reservas
    'huespedes',  # Módulo 6: huéspedes, check-in, consumos y check-out
    'caja',       # Módulo 7: cobros y caja
    'pedidos',    # Módulo 8: pedidos y reclamos
    'reportes',   # Módulo 9: reportes para el Gerente
]

# Middleware: "filtros" por los que pasa cada pedido (sesiones, seguridad, login, mensajes...).
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo donde empiezan todas las rutas (URLs) del sitio.
ROOT_URLCONF = 'sgh.urls'

# Templates: Django busca los HTML en la carpeta templates/ de la raíz
# y también en la carpeta templates/ de cada app (APP_DIRS).
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Punto de entrada para servidores web (no hace falta tocarlo).
WSGI_APPLICATION = 'sgh.wsgi.application'


# Base de datos MySQL. Los datos de conexión se leen del .env.
# utf8mb4 permite guardar cualquier carácter (tildes, ñ, emojis).
# STRICT_TRANS_TABLES hace que MySQL rechace datos inválidos en vez de recortarlos en silencio.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'sgh'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        # Base temporal que crea "python manage.py test" (se llama test_sgh y se borra al terminar).
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        },
    }
}


# Reglas que deben cumplir las contraseñas de los usuarios.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Idioma y zona horaria: español de Argentina, hora de Córdoba.
# USE_TZ guarda las fechas en UTC en la base y las muestra en la hora local.
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Cordoba'
USE_I18N = True
USE_TZ = True


# Archivos estáticos (CSS, JavaScript, imágenes del diseño): están en la carpeta static/.
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Archivos subidos por los usuarios (por ejemplo, fotos de las unidades): se guardan en media/.
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Tipo de campo para los id automáticos de cada tabla.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Usuario personalizado (con rol) en lugar del que trae Django.
# IMPORTANTE: tiene que estar definido antes de la primera migración.
AUTH_USER_MODEL = 'usuarios.Usuario'

# Login y logout: a dónde se manda al usuario (son nombres de rutas definidas en sgh/urls.py).
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'inicio'
LOGOUT_REDIRECT_URL = 'login'


# Mensajes (messages.success, messages.error...): "error" se traduce a "danger"
# para que coincida con los colores de las alertas de Bootstrap.
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
