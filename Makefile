run:
	pdm run python -m adapters.handlers.rest.app

setup:
	pdm install

lint:
	pdm run ruff check

test:
	pdm run pytest