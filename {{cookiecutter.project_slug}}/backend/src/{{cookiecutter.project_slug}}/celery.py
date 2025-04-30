import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_slug}}.settings.develop"
)

app = Celery("{{cookiecutter.project_slug}}")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()

# Example beat schedule. Replace with functional code
app.conf.beat_schedule = {  # type: dict[str, dict[str, Any]
    "multiply-task-crontab": {
        "task": "multiply_two_numbers",
        "schedule": crontab(hour=7, minute=30, day_of_week=1),
        "args": (16, 16),
    },
    "multiply-every-5-seconds": {
        "task": "multiply_two_numbers",
        "schedule": 5.0,
        "args": (16, 16),
    },
    "add-every-30-seconds": {
        "task": "{{cookiecutter.project_slug}}.tasks.add",
        "schedule": 30.0,
        "args": (16, 16),
    },
}
