"""
Django settings for social_app project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta

from decouple import Csv, config
from django.core.management.utils import get_random_secret_key
import ssl

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import cloudinary
import cloudinary.uploader
import cloudinary.api


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key(), cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="IP", cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'air_quality_app',
    'core',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'import_export',
    'django_celery_results',
    'django_celery_beat',
    'cloudinary',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'config.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'social_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'social_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DATABASE_NAME"),
        "USER": config("DATABASE_USER"),
        "PASSWORD": config("DATABASE_PASSWORD"),
        "HOST": config("DATABASE_HOST"),
        "PORT": config("DATABASE_PORT"),
        "OPTIONS": {"sslmode": "require"},
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

## swagger ui
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Basic": {"type": "basic"},
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
    "USE_SESSION_AUTH": True,
    "LOGIN_URL": "admin/",
    "LOGOUT_URL": "admin/logout/",
}
REDOC_SETTINGS = {
    "LAZY_RENDERING": False,
    "FETCH_SCHEMA_WITH_QUERY": True,
    "REQUIRED_PROPS_FIRST": True,
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Dajgno User Config
AUTH_USER_MODEL = 'core.User'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "core.authentication.CustomTokenAuthentication",
    ),

}

# CELERY
REDIS_PASS=config("REDIS_PASS")
REDIS_HOST_PORT_URL=config("REDIS_HOST_PORT_URL")
_broker_url = f'rediss://:{REDIS_PASS}@{REDIS_HOST_PORT_URL}'
BROKER_URL = _broker_url
CELERY_RESULT_BACKEND = _broker_url
BROKER_USE_SSL={'ssl_cert_reqs': ssl.CERT_NONE}
CELERY_REDIS_BACKEND_USE_SSL={'ssl_cert_reqs': ssl.CERT_NONE}


ENVIRONMENT="developments"

SIMPLE_JWT = {
    # 'ACCESS_TOKEN_LIFETIME': timedelta(seconds=10),
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=50),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5) if ENVIRONMENT == "production" else timedelta(days=100),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
}

# CORS
CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=Csv())
CSRF_COOKIE_DOMAIN = config('CSRF_COOKIE_DOMAIN')
SECURE_SSL_REDIRECT = \
    config('SECURE_SSL_REDIRECT', '0').lower() in ['true', 't', '1']
if SECURE_SSL_REDIRECT:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# CORS_ALLOWED_ORIGINS = [
#     "https://6490-102-88-35-217.ngrok-free.app",
#     "http://localhost:8081",
#     "http://127.0.0.1:8081"
# ]
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^https://\w+\.domain\.com$",
# ]
# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]
# CORS_ALLOW_HEADERS = [
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# ]

IPINFO_TOKEN = config("IPINFO_TOKEN")
AQI_TOKEN = config("AQI_TOKEN")

cloudinary.config( 
  cloud_name = config("CLOUDINARY_CLOUD_NAME"),
  api_key = config("CLOUDINARY_API_KEY"),
  api_secret = config("CLOUDINARY_API_SECRET")
)