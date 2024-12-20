run:
	pdm run python -m adapters.handlers.rest.app

lint:
	pdm run ruff check

test:
	pdm run pytest