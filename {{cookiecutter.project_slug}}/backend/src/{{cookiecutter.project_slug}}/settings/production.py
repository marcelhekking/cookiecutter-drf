import os  # noqa

from .base import *  # noqa
import environ

env = environ.Env()

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("SQL_DATABASE", "database"),
        "USER": os.getenv("SQL_USER", "user"),
        "PASSWORD": os.getenv("SQL_PASSWORD", "password"),
        "HOST": os.getenv("SQL_HOST", "localhost"),
        "PORT": os.getenv("SQL_PORT", "5432"),
    }
}

ALLOWED_HOSTS = [
    "localhost",
]

STATIC_ROOT = "../public/staticfiles/"

MEDIA_ROOT = "../public/mediafiles/"

LOGGING = {  # noqa
    "version": 1,
    "disable_existing_loggers": False,
    "django": {
        "handlers": ["django"],
        "level": "INFO",
        "propagate": True,
    },
}

CSRF_TRUSTED_ORIGINS = ["https://example.com"]
