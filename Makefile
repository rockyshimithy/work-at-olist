SHELL=/bin/bash

help:
	@echo 'Makefile for telephone bill issuer                            '
	@echo '                                                              '
	@echo 'Usage:                                                        '
	@echo '    make clean              Remove python compiled files      '
	@echo '    make requirements       Install required packages         '
	@echo '    make requirements_dev   Install required packages to Dev  '
	@echo '    make unit               Run unit tests                    '
	@echo '    make superuser          Create admin user on Django       '
	@echo '    make migrate_db         Apply the migrations to db        '
	@echo '    make runserver          Run the application               '
	@echo '                                                              '


clean:
	find . -iname *.pyc -delete
	find . -iname *.pyo -delete
	find . -iname __pycache__ -delete
	rm -fr .cache;


requirements:
	pip install -r requirements.txt

requirements_dev:
	pip install -r requirements_dev.txt


unit:clean
	py.test tests/ -v


superuser:
	python manage.py createsuperuser

migrate_db:
	python manage.py migrate

runserver:
	python manage.py runserver
