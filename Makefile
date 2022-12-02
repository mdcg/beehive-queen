install:
	@poetry install

run:
	@poetry run python -m server

tests/unit:
	@poetry run pytest test/unit

tests/integration:
	@poetry run pytest test/integration

tests:
	tests/unit
	tests/integration
