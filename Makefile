install:
	poetry install
	poetry shell

lint:
	black yatzy tests
	mypy yatzy
	pylint yatzy

test:
	coverage run --module unittest
	coverage report

ci: install lint test
