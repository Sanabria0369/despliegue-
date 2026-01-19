from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-key'

DEBUG = False

ALLOWED_HOSTS = ['.vercel.app', 'localhost']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'analyzer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'svm_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'analyzer' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': []},
    },
]

WSGI_APPLICATION = 'svm_django.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
