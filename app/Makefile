# makefile

init: 
	pip install --upgrade pip
	pip install -r _requirements/base.txt -r _requirements/develop.txt
	mkdir -p data/static data/media
	rm -rf sso
	ln -s ../django_utils/app/sso sso
	make migrate

loaddata:
	python manage.py loaddata _fixtures/polls.json

dumpdata:
	python manage.py dumpdata polls --indent 2 > _fixtures/polls.json

run:
	make precommit
	python manage.py runserver 0.0.0.0:8000

precommit:
	black --line-length=140 .
	flake8 --ignore E501 --exclude 'core/settings/*' .

migrations:
	python manage.py makemigrations
	make precommit

migrate:
	python manage.py migrate

update:
	pur -r _requirements/base.txt
	pur -r _requirements/production.txt
