.PHONY: format lint install-hooks precommit

format:
	uv run ruff format .

lint:
	uv run ruff check .

install-hooks:
	uv run pre-commit install

precommit:
	uv run pre-commit run --all-files
