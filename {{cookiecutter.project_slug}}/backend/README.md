# Cookiecutter DRF

## Introduction

This part is the backend of the Cookiecutter DRF project.

## Installation and development

### Installation

#### Install and run the Django development server locally for the first time

Go to the backend root of the project (`{{cookiecutter.project_slug}}\backend`) and install all dependencies specified in the `pyproject.toml`, create the database, perform migrations, and create an initial superuser ( This is the person as specified in the `ADMINS` list in `base.py`) with the following make command:

```bash
make install
```

Connect to the Django admin running on local host: `http://localhost:8000/admin/`. Login with name of the admin specified in `ADMINS` and the password `OnlyValidLocally`.

#### Start Django development server locally after installation

For subsequent starts of the local development server of Django use:

```bash
make runserver
```

### Development

Ruff is used for Python formatting and linting. To prevent unstyled Python code to enter a Git repo, [pre-commit](https://pre-commit.com/) is used

#### Installing Pre-commit

In the activated Python virtual environment, go to the root of the project (`{{cookiecutter.project_slug}}\backend`) and run:

```bash
pre-commit install
```

To test, you can check existing files with pre-commit:

```bash
pre-commit run --all-files
```

## Running the container in production mode locally

With Docker, you can start a container in production mode.

### Setting up Nginx

The container starts a gunicorn server downstreams serving all Django requests. Nginx can then be configured to run as a proxy-server on your machine to forward all requests to the gunicorn server while serving the media- and staticfiles by its own. Example Nginx config (this assumes that `omni.local` has been added to the hosts file on your machine):

```bash
server {
    gzip            off;
    server_name     omni.local;

    location / {
        proxy_pass http://localhost:8000/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
        client_max_body_size 100M;
    }

    location /static/ {
        alias /home/<user home folder>/www/omni/public/staticfiles/;
    }

    location /media/ {
        alias /home/<user home folder>/www/omni/public/mediafiles/;
    }
}
```

### Create public static and media folders

In the Docker files, a physical volume on the host is linked with folders inside Docker. The web Docker performs actions under GI 1024 (e.g., running `collectstatic`).  To avoid permission errors:

- Create a static files and mediafiles folder on your machine (defaults are `~/www/omni/public/mediafiles/`, and `~/www/omni/public/staticfiles/` which work with the sample Nginx configuration file as shown above),
- Set correct permission of the folder.

This can be done with:

```bash
make public
make 1024
```

### Starting the containers in production mode

Go to the backend root of the project (`{{cookiecutter.project_slug}}\backend`) and first (only to be done once) build the container with:

```bash
make build
```

Then start the container with:

```bash
make up
```

and shut it down with:

```bash
make down
```
