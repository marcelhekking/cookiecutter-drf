"""
Django settings for {{cookiecutter.project_slug}} Website.

"""

import os
import sys
from pathlib import Path

# Automatically figure out the ROOT_DIR and PROJECT_DIR.
path = Path(__file__)

DJANGO_PROJECT_DIR = path.parent.parent
SRC_DIR = DJANGO_PROJECT_DIR.parent
ROOT_DIR = DJANGO_PROJECT_DIR.parent.parent


ADMINS = [
    (
        "{{cookiecutter.author_first_name.lower()}}",
        "{{cookiecutter.author_email.lower()}}",
    ),
]

SECRET_KEY = os.getenv("SECRET_KEY", "a key")

SITE_ID = 1

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

DEBUG = os.getenv("DEBUG", False)

# Application definition

INSTALLED_APPS = [
    # project apps...
    "{{cookiecutter.project_slug}}",
    "{{cookiecutter.project_slug}}.users",
    # Third party apps
    "django_celery_beat",
    "django_celery_results",
    "rest_framework",  # utilities for rest apis
    "rest_framework.authtoken",  # token authentication
    "drf_spectacular",
    # Django apps...
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{cookiecutter.project_slug}}.urls"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.DefaultStorageFinder",
]

STATICFILES_DIRS = (str(SRC_DIR / "static"),)

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = str(ROOT_DIR / "/local/staticfiles")
MEDIA_ROOT = str(ROOT_DIR / "local/mediafiles")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(SRC_DIR / "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.static",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "{{cookiecutter.project_slug}}.wsgi.application"

FIXTURE_DIRS = Path(ROOT_DIR) / "tests"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
TIME_ZONE = "Europe/Amsterdam"
USE_I18N = True

LANGUAGE_CODE = "nl"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (str(SRC_DIR / "locale"),)

LOGIN_REDIRECT_URL = "/"

# Custom user app
AUTH_USER_MODEL = "users.User"

# Django Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": int(os.getenv("DJANGO_PAGINATION_LIMIT", 10)),
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# Celery
# save Celery task results in Django's database
CELERY_RESULT_BACKEND = "django-db"

# This configures Redis as the datastore between Django + Celery
CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_REDIS_URL", default="redis://localhost:6379"
)

# this allows you to schedule items in the Django admin.
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"

# DRF Spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "{{cookiecutter.project_name}}",
    "DESCRIPTION": "{{cookiecutter.description}}",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# Debug Toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Debug toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Define a flag to check if tests are running
TESTING = any(True for arg in sys.argv if "test" in arg) or any(
    True for arg in sys.argv if "pytest" in arg
)
