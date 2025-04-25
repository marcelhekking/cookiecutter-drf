# {{cookiecutter.project_name}}

## Introduction

{{cookiecutter.description}}

## Installation and development

### Installation

#### Install and run the Django development server locally for the first time

Go to the backend root of the project (`{{cookiecutter.project_slug}}/backend`) and install all dependencies specified in the `pyproject.toml`, create the database, perform migrations, and create an initial superuser ( This is the person as specified in the `ADMINS` list in `base.py`) with the following make command:

```bash
make install
```

#### Start Django development server locally

For starting the local development server of Django use:

```bash
make runserver
```

Connect to the Django admin running on local host: `http://localhost:8000/admin/`. Login with name of the admin specified in `ADMINS` and the password `OnlyValidLocally`.

#### Start Celery and Redis

You can spin up a Redis container and a Celery worker which allows you to run (asynchronous) tasks.

Go to the backend root of the project (`{{cookiecutter.project_slug}}/backend`) and start the Redis container and a Celery worker with:

```bash
make redis_up
make celery
```

or

```bash
make start_celery
```

You will see that Celery will spawn little math tasks regularly as a test. You can find them in `tasks.py` so you can remove them.

CTRD-D to shutdown Celery and  `make redis_down` to stop and remove the Redis container.

### Development

Ruff is used for Python formatting and linting. To prevent unstyled Python code to enter a Git repo, [pre-commit](https://pre-commit.com/) is used

#### Installing Pre-commit

In the activated Python virtual environment, go to the root of the project (`{{cookiecutter.project_slug}}/backend`) and run:

```bash
pre-commit install
```

To test, you can check existing files with pre-commit:

```bash
pre-commit run --all-files
```

## Running the container in production mode locally

With Docker, you can start a container in production mode.

### First time running

Go to the root of the project (`{{cookiecutter.project_slug}}/backend`) and run these commands:

- Install dependencies: `uv sync`
- Create public directory for mediafiles and staticfiles: `make public`
- Create the build: `make build`
- Set environment variables: `export $(grep -v '^#' .env_var | xargs)`
- Start Nginx and run the app: `make start`

Connect to the Django admin running on local host: `http://localhost/admin`. Login with name of the admin specified in `ADMINS` and the password `OnlyValidLocally`.

To stop and remove all containers:

- `make stop`

### Starting containers after first time running

For subsequent starts of the containers use:

- `make start`
