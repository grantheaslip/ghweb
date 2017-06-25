import builtins
import logging.config
import os
import sys
from pathlib import Path
from pprint import pprint

# Globally alias `pprint.pprint()` as `pp()` for debugging
builtins.pp = pprint

BASE_DIR = Path(__file__).resolve().parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[1]

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ['*']

CANONICAL_HOST = os.environ.get('CANONICAL_HOST')
CANONICAL_SCHEME = os.environ.get('CANONICAL_SCHEME')

using_default_log_level = False

try:
    LOG_LEVEL = os.environ['LOG_LEVEL']
except KeyError:
    LOG_LEVEL = 'WARNING'
    using_default_log_level = True

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'personal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'ghweb.middleware.CanonicalSchemeAndHostMiddleware',
    'django.middleware.common.CommonMiddleware',
    'ghweb.middleware.ExceptionLoggingMiddleware',
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

LOGGING_CONFIG = None
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": True,
    'formatters': {
        'custom': {
            'format': '[%(asctime)s %(levelname)s %(name)s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M'
        },
        'custom_server': {
            'format': '    %(message)s',
            'datefmt': '%Y-%m-%d %H:%M'
        },
    },
    "handlers": {
        # Redefine console logger to run in production.
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'custom',
            'stream': sys.stdout,
            'level': LOG_LEVEL,
        },
        'console_server': {
            'class': 'logging.StreamHandler',
            'formatter': 'custom_server',
            'stream': sys.stdout,
            'level': LOG_LEVEL,
        },
    },
    "loggers": {
        # Redefine django logger to use redefined console logging.
        '': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True
        },
        'django.server': {
            'handlers': ['console_server'],
            'level': LOG_LEVEL,
            'propagate': False
        },
    }
})

if using_default_log_level:
    import logging
    logger = logging.getLogger(__name__)

    logger.warning(
        'Using default log level of WARNING since LOG_LEVEL environment ' +
        'variable wasn’t set'
    )
