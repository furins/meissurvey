.PHONY: run, upgrade, install, check, theme, dev

install:
	python -m pip install -U -r requirements/production.txt

upgrade: check
	python manage.py migrate

check: install
	python manage.py makemigrations
	python manage.py collectstatic --noinput

theme: upgrade
	python manage.py tailwind start

run: upgrade
	python manage.py runserver

build: upgrade
	python manage.py tailwind build

dev:
	python -m pip install -U -r requirements/development.txt
	$(MAKE) install