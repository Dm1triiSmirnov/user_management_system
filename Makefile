install:
	poetry install

lint:
	poetry run flake8

format:
	poetry run black .
	poetry run isort .

run:
	poetry run python3 manage.py runserver

