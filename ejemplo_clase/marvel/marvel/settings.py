"""
Django settings for marvel project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
# NOTE: Importamos os para indicar el directorio de templates y otras utilidades:
import os
# Importamos Celery para el manejo de tareas asincrónicas:
from celery.schedules import crontab


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$dpguq$#6!6dw($(qd6))7qcw%%#a=sc!-!7t!_av9%5*(q=uf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps: Acá ponemos el nombre de las carpetas de nuestras aplicaciones
    'e_commerce',
    # Third party apps: acá vamos agregando las aplicaciones de terceros, extensiones de Django.
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'marvel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # NOTE: Agregamos el directorio para los templates, necesario para Swagger
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'marvel.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'marvel_db',        # POSTGRES_DB
        'USER': 'inove_user',      # POSTGRES_USER
        'PASSWORD': '123Marvel!',  # POSTGRES_PASSWORD
        'HOST': 'db',                # Nombre del servicio
        'PORT': '5432'              # Número del puerto
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# NOTE: STATIC_ROOT y STATICFILES_DIRS No pueden contener el mismo directorio entre sus variables.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (str(BASE_DIR.joinpath('staticfiles')),)


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# NOTE: Para debug
# Color en los prints:
# Modo de uso: print(VERDE+"mi texto")

AMARILLO = "\033[;33m"
CIAN = "\033[;36m"
VERDE = "\033[;32m"

# NOTE: Para manejo de sesión.
LOGIN_REDIRECT_URL = '/e-commerce/index'
LOGIN_URL = '/e-commerce/'

# NOTE: Logging settings

LOGGING_DIR = f'{BASE_DIR}/marvel/logs/'

SIMPLE_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'generic': {
            'format': '[%(asctime)s] |%(levelname)s| %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S",
            'style': '%'
        }
    },
    'handlers': {
        'general': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'general.log'),
            'formatter': 'generic'
        }
    },
    'loggers': {
        # django: registra todos los logs
        'django': {
            'handlers': ['general'],
            'propagate': True,
            'level': 'DEBUG',
        }
    }
}

COMPLEX_LOGGING = {
    # NOTE: Establecemos la versión:
    'version': 1,
    # NOTE: Mantenemos el resto de los loggers:
    'disable_existing_loggers': False,
    # NOTE: Generamos filtros de estado de debug:
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # NOTE: Diseñamos formateadores para los mensajes:
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'time': {
            'format': '[%(asctime)s] |%(levelname)s| %(message)s'
        },
        'generic': {
            'format': '[%(asctime)s] |%(levelname)s| %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S",
            'style': '%'
        }

    },
    # NOTE: Generamos manejadores para los distintos tipos de mensajes:
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'generic'
        },
        # general: Para registrar todos los mensajes.
        'general': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'general.log'),
            'formatter': 'generic'
        },
        # requests: para los mensajes del servidor:
        'requests': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'requests.log'),
            'formatter': 'time',
        },
        # site: Para registrar los errores en el render de las variables de los templates.
        'site': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'template-rendering.log'),
            'formatter': 'time',
        },
        # database: Registra las consultas en la base de datos [solo para debug]
        'database': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'database.log'),
            'formatter': 'time',
        },
        # security: registra las operaciones sospechosas.
        'security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'security.log'),
            'formatter': 'time',
        },
        # generalbatch: Para registrar todos los mensajes, pero limita los logs a 15MB
        # Luego, fracciona el log en 10 partes segun backupCount.
        'generalbatch': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'general-batch.log'),
            'maxBytes': 1024*1024*15,  # 15MB
            # 'maxBytes': 1024,
            'backupCount': 10,
            'formatter': 'generic',
        },
    },
    # NOTE: Ahora establecemos los loggers:
    'loggers': {
        # django: registra todos los logs
        # 'django': {
        #     'handlers': ['general', 'console'],
        #     'propagate': True,
        #     'level': 'DEBUG',
        # },
        # django.server: filtra los mensajes del servidor
        'django.server': {
            'handlers': ['requests', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # django.template: para los mensajes de renderizado de templates
        'django.template': {
            'handlers': ['site'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # django.db.backends: registra las querys a la base de datos
        'django.db.backends': {
            'handlers': ['database'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # django.security.csrf: registra errores csrf en formularios.
        'django.security.csrf': {
            'handlers': ['security'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # django: registra todos los logs, pero en hasta 10 lotes de 15MB
        'django': {
            'handlers': ['generalbatch'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

# NOTE: Ejemplo de aplicación en API Test logging.
LOGGING = SIMPLE_LOGGING # COMPLEX_LOGGING

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Argentina/Buenos_Aires'

CELERY_BEAT_SCHEDULE = {
    'hello': {
        'task': 'e_commerce.tasks.hello_world',
        'schedule': crontab(minute='*/2')  # Cada 2 minutos ejecutar
    },
    'segunda_tarea': {
        'task': 'e_commerce.tasks.segunda_tarea',
        'schedule': crontab(minute='*/1')  # Cada 60 minutos ejecutar
    }
}

