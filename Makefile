.PHONY: install
install:
	poetry install
	poetry run pre-commit install

PHONY: format
format:
	poetry run black .
	poetry run isort .

PHONY: lint
lint:
	poetry run black --check .
	poetry run isort --check-only .
