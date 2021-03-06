import os
from decouple import config, Csv
from dj_database_url import parse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_auth',
    'rest_framework.authtoken',
    'django_filters',
    'django_extensions',
    'django_celery_beat',
    'django_celery_results',
]

LOCAL_APPS = [
    'core',
    'crm',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS
AUTH_USER_MODEL = 'core.User'


REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'COERCE_DECIMAL_TO_STRING': False,
}

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'core.serializers.TokenSerializer',
    'USER_DETAILS_SERIALIZER': 'core.serializers.UserSerializer',
}

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'api.wsgi.application'

DEFAULT_DATABASE = 'sqlite:///' + os.path.join(BASE_DIR, 'docsapp.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', cast=parse, default=DEFAULT_DATABASE)
}

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

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_PATH = config('STATIC_PATH', default='static')
MEDIA_PATH = config('MEDIA_PATH', default='media')

STATIC_URL = f'/{STATIC_PATH}/'
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_PATH)

MEDIA_URL = f'/{MEDIA_PATH}/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_PATH)

EMAIL_BACKEND = config('MAIL_BACKEND')
EMAIL_HOST = config('MAIL_HOST')
DEFAULT_FROM_EMAIL = config('MAIL_DEFAULT_FROM')
SERVER_EMAIL = config('MAIL_SERVER')
EMAIL_HOST_USER = config('MAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('MAIL_HOST_PASSWORD')
EMAIL_PORT = config('MAIL_PORT', cast=int)
EMAIL_USE_TLS = config('MAIL_USE_TLS', cast=bool)


BROKER_URL = config('BROKER_URL')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = config('CELERY_TASK_SERIALIZER', default='json')
CELERY_RESULT_SERIALIZER = config('CELERY_RESULT_SERIALIZER', default='json')
CELERY_TIMEZONE = config('CELERY_TIMEZONE', default='America/Cuiaba')
CELERY_BEAT_SCHEDULE = config('CELERY_BEAT_SCHEDULE', default={})