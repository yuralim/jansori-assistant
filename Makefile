.PHONY: format lint test test-integration install-hooks precommit db-up db-down db-clean db-migrate db-revision

format:
	uv run ruff format .

lint:
	uv run ruff check .

test:
	uv run pytest

test-integration:
	uv run pytest integration_tests

install-hooks:
	uv run pre-commit install

precommit:
	uv run pre-commit run --all-files

db-up:
	docker compose up -d postgres

db-down:
	docker compose down

db-clean:
	docker compose down -v

db-migrate:
	uv run alembic upgrade head

db-revision:
	uv run alembic revision --autogenerate -m "$(m)"
