install:
	poetry install

lint:
	poetry run flake8 authentication tests users user_management_system

format:
	poetry run black authentication tests users user_management_system
	poetry run isort authentication tests users user_management_system

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	poetry run python3 manage.py runserver

run-tests:
	poetry run pytest -vvv
