import builtins
import os
from pathlib import Path
from pprint import pprint

# Globally alias `pprint.pprint()` as `pp()` for debugging
builtins.pp = pprint

BASE_DIR = Path(__file__).resolve().parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[1]

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'personal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'ghweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'ghweb.context_processors.app_name_and_version',
            ],
        },
    },
]

WSGI_APPLICATION = 'ghweb.wsgi.application'

TIME_ZONE = 'America/Toronto'
USE_TZ = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'personal.utils.CompressedManifestStaticFilesStorage'
WHITENOISE_ALLOW_ALL_ORIGINS = False
WHITENOISE_ROOT = BASE_DIR / 'personal' / 'static_root'
