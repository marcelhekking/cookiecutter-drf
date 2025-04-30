# Cookiecutter template for starting a Django restful API application

## Introduction

This repo is a cookiecutter template to create a Django restful API application based on the [Django REST framework](<https://www.django-rest-framework.org/>). The application structure is that of a mono repo holding both the backend as well as the frontend part of the applicaton. Moreover, [Sphinx](<https://www.sphinx-doc.org/en/master/>) is installed to enable the documentation of the project.

## What's included?

- [Django REST framework](<https://www.django-rest-framework.org/>)
- Documentation with [Sphinx](<https://www.sphinx-doc.org/en/master/>)
- Dependency management with [uv](https://docs.astral.sh/uv/)
- [Pre-commit](https://pre-commit.com/) hooks
- [Drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/readme.html) to document your APIs according to the OpenAPI standard
- A selection of [Make](https://www.gnu.org/software/make/) commands to control various aspect of the application
- [Docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/) to start a production container locally
- [Celery](https://github.com/celery/celery) and [Celery Beat](https://docs.celeryq.dev/en/latest/userguide/periodic-tasks.html) for kicking off periodic (asynchronous) tasks
- [Django Celery Results](https://github.com/celery/django-celery-results) for capturing Celery tasks in the database
- [Flower](https://flower.readthedocs.io/en/latest/) via a container for monitoring Celery tasks
- [Redis](https://redis.io/) via a container
- [Nginx](https://nginx.org/) via a container to function as a reverse-proxy for the [Gunicorn](https://gunicorn.org/) Django server upstreams
- [Ruff](https://docs.astral.sh/ruff/) for Python linting and formatting
- [Pytest](https://docs.pytest.org/en/stable/) for testing
- [Ctrl-z](https://ctrl-z.readthedocs.io/en/latest/) for making backups of the [PostgreSQL](https://www.postgresql.org/) database
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) for...well...debugging

## How to install this template

First install [uv](https://docs.astral.sh/uv/#installation) on your system and then run:

```bash
uvx cookiecutter gh:marcelhekking/cookiecutter-drf
```

You'll be asked some questions about the project. After installation, read the README.md file of the just created project on how to further set things up. There are basically two ways to get the project running: one by using Docker and the other one by starting Django as a deveopment server.
