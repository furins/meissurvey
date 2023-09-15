.PHONY: run, upgrade, install, check, theme, dev, translate

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
	python manage.py collectstatic --noinput

dev:
	python -m pip install -U -r requirements/development.txt
	python manage.py tailwind install
	$(MAKE) install

translate:
	mkdir -p rosetta/locale/{it,en}/LC_MESSAGES
	python manage.py makemessages -l en
	python manage.py makemessages -l it
