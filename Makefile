install:
	pip install -r requirements.txt

lint:
	black src tests
	mypy src
	pylint src

test:
	coverage run --source=src --module unittest
	coverage report

ci: install lint test
