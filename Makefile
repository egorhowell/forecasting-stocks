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

PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	git add requirements.txt

PHONY: lock
lock:
	poetry lock
	git add poetry.lock