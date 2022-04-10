install:
	pip install -e '.[test]'

lint:
	black yatzy tests
	mypy yatzy
	pylint yatzy

test:
	coverage run --source=yatzy --module unittest
	coverage report

ci: install lint test
