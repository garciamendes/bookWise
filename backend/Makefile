# Docker
run-docker:
	docker compose --env-file .env -f docker-compose.yml up -d

# Django
runserver: run-docker
	./manage.py runserver 0.0.0.0:8000

migrate: run-docker
	./manage.py migrate

migrations: run-docker
	./manage.py makemigrations

test: run-docker
	./manage.py test

superuser:
	./manage.py createsuperuser

urls:
	./manage.py show_urls

shell:
	./manage.py shell_plus

shell-sql:
	./manage.py shell_plus --print-sql

collectstatic:
	./manage.py collectstatic --noinput
