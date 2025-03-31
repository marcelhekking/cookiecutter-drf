# Cookiecutter template for starting a Django restful API application

## Introduction

This repo is a cookiecutter template to create a Django restful API application based on the Django REST framework (<https://www.django-rest-framework.org/>). The application structure is that of a mono repo holding both the backend as well as the frontend part of the applicaton. Moreover, Sphinx (<https://www.sphinx-doc.org/en/master/>) is installed to enable the documentation of the project.

## How to install this template

First install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and then run:

```bash
cookiecutter https://github.com/marcelhekking/cookiecutter-drf
```

You'll be asked some questions about the project. After installation, read the README.md file of the just created project on how to further set things up. There are basically two ways to get the project running: one by using Docker and the other one by starting Django as a deveopment server.
