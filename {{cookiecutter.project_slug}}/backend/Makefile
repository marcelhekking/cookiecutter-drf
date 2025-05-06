DATABASE_NAME ?= {{cookiecutter.project_slug}}

.PHONY: all clean install requirements


all: clean install compilemessages exampledata

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' | xargs rm -rf

#
# Django development server
#
rebuild:
	dropdb --if-exists $(DATABASE_NAME)
	createdb $(DATABASE_NAME)
	uv run manage.py migrate
	uv run manage.py initadmin

install:
	uv sync
	createdb $(DATABASE_NAME)
	uv run manage.py migrate
	uv run manage.py initadmin

makemigrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

runserver:
	uv run manage.py runserver

test:
	uv run pytest tests/

#
# Docker
#
public:
	mkdir -p ./public/staticfiles
	mkdir -p ./public/mediafiles
	# 1024 is the group id of the docker container
	sudo chown -R :1024 ./public/mediafiles
	sudo chmod -R 775 ./public/mediafiles
	sudo chmod g+s ./public/mediafiles
	sudo chown -R :1024 ./public/staticfiles
	sudo chmod -R 775 ./public/staticfiles
	sudo chmod g+s ./public/staticfiles

build:
	sudo docker build -t {{cookiecutter.project_slug}}-web:latest -f Dockerfile .

app_up_fish:
	fish -c 'envsource .env_var; and docker compose -p {{cookiecutter.project_slug}} -f docker-compose.yml up -d'

app_down_fish:
	fish -c 'envsource .env_var; and docker compose -p {{cookiecutter.project_slug}} -f docker-compose.yml down'

app_up:
	# assuming environment variables are set with `export $(grep -v '^#' .env_var | xargs)`
	docker compose -p {{cookiecutter.project_slug}} -f docker-compose.yml up -d

app_down:
	# assuming environment variables are set with `export $(grep -v '^#' .env_var | xargs)`
	docker compose -p {{cookiecutter.project_slug}} -f docker-compose.yml down

app_sh:
	docker exec -it {{cookiecutter.project_slug}}-web-1 sh

app_shell:
	docker exec -it {{cookiecutter.project_slug}}-web-1 python manage.py shell

#
# Format / Lint targets
#
mypy:
	mypy src/{{cookiecutter.project_slug}}

format: format_backend format_sort

format_backend: ruff sort

format_sort: sort

sort: sort_fix

sort_check:
	uv run ruff check src tests --target-version=py313 --exclude=migrations --select I

sort_fix:
	uv run ruff check src tests --target-version=py313 --exclude=migrations --select I --fix

ruff: ruff_fix

ruff_check:
	uv run ruff check src tests --target-version=py313 --exclude=migrations

ruff_fix:
	uv run ruff check src tests --target-version=py313 --exclude=migrations --fix

#
# Celery / Redis / Flower
#
celery:
	celery -A {{cookiecutter.project_slug}} worker -l info --beat

redis_up:
	docker compose -p {{cookiecutter.project_slug}} -f docker-compose-redis-only.yml up -d

redis_down:
	docker compose -p {{cookiecutter.project_slug}} -f docker-compose-redis-only.yml down

start_celery: redis_up celery

flower_up:
	docker compose -p {{cookiecutter.project_slug}} -f docker-compose-flower-only.yml up -d

flower_down:
	docker compose -p {{cookiecutter.project_slug}} -f docker-compose-flower-only.yml down


#
# Nginx
#
nginx_up:
	docker compose -p {{cookiecutter.project_slug}} -f docker-compose-nginx-only.yml up -d

nginx_down:
	docker compose -p {{cookiecutter.project_slug}} -f docker-compose-nginx-only.yml down

#
# Docker / Nginx
#
start: nginx_up app_up

stop: nginx_down app_down

start_fish: nginx_up app_up_fish

stop_fish: nginx_down app_down_fish

#
# API Documentation with Swagger
#
swagger:
	uv run manage.py spectacular --color --file schema.yml
	docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui

