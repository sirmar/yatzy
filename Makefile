install:
	pip install -r requirements.txt

lint:
	pylint src tests
	black src tests
	mypy src

test:
	coverage run --source=src --module unittest
	coverage report

ci: lint test
