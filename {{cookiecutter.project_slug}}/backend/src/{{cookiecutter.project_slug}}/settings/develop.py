import os  # noqa
from .base import *  # noqa
import environ

DJANGO_SETTINGS_MODULE = "{{cookiecutter.project_slug}}.settings.develop"
DEBUG = True
env = environ.Env()


DATABASES = {"default": env.db(default="postgresql://localhost/{{cookiecutter.project_slug}}")}


LOGGING = {  # noqa
    "version": 1,
    "disable_existing_loggers": False,
    "django": {
        "handlers": ["django"],
        "level": "INFO",
        "propagate": True,
    },
}


# Debug Toolbar
if not TESTING:
    # only install debug toolbar if not testing
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "debug_toolbar",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]
