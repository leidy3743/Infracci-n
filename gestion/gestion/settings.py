# -*- coding: utf-8 -*-
"""
Django settings for gestion project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%_gq=i!#=99l58@!4hw=#ounsw=tsdlq)mvk@_mrx+j(z1u9wo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

#Enviar correo electrónico para contraseñas olvidadas
#Es necesario configurar tu cuenta para permitir que django la use para enviar correos
#Permite activar las aplicaciones inseguras en su cuenta de google(esto hace que su cuenta sea vulnerable)
"""EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 25 #Raises an error that I can not solve yet (SMTP AUTH extension not supported by server)
EMAIL_PORT = 587
EMAIL_HOST_USER = 'leidy3743@gmail.com'
EMAIL_HOST_PASSWORD = 'andrecito'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGIN_URL = "/inicio/login/"
USE_DJANGO_JQUERY = False"""


# Application definition
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'django.contrib.humanize',
    'inicio',
    'cuenta',
    'persona',
    'infraccion',
    'rest_framework',
]

BOOTSTRAP3 = {
    'required_css_class': 'required',
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

ROOT_URLCONF = 'gestion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],

        },
    },
]

WSGI_APPLICATION = 'gestion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'bdtransito',

    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#Archivos estáticos (CSS, JavaScript, Images
#https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'

#Lugares adicionales para collectstatic para encontrar archivos estáticos.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

#Para implementación
STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = os.path.join(STATIC_ROOT, "media")
MEDIA_URL = '/media/'

#Para la depuración
#STATIC_ROOT = os.path.join(BASE_DIR, "static")
#MEDIA_ROOT = os.path.join(BASE_DIR, "media")
#MEDIA_URL = '/media/'


#Humanizar la configuración
USE_THOUSAND_SEPARATOR = True

#http://stackoverflow.com/questions/22476273/no-access-control-allow-origin-header-is-present-on-the-requested-resource-i
CORS_ORIGIN_ALLOW_ALL = True

#Actualizar la configuración de la base de datos con $DATABASE_URL.
#import dj_database_url
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
