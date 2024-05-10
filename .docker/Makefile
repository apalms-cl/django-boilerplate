# makefile

build:
	docker-compose --file dc-produccion.yml --project-name b up -d --build --force-recreate --remove-orphans
	docker ps

_build:
	docker-compose --project-name boilerplate up -d --build --force-recreate --remove-orphans
	docker exec boilerplate python manage.py migrate
	docker exec boilerplate make precommit
	docker ps

_admin:
	docker exec boilerplate bash -c "echo \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')\" | python manage.py shell"

update:
	git submodule update
	git stash
	git pull
	git stash pop

logs:
	docker logs -f boilerplate

ssh:
	docker exec -it boilerplate bash
