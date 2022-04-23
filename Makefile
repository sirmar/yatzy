install:
	poetry install

lint:
	black yatzy tests
	mypy yatzy
	pylint yatzy

test:
	coverage run --module unittest
	coverage report

ci: install lint test
