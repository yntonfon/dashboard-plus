clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

start:
	python run.py

install:
	pip install -r requirements.txt
	pip install -r dev-requirements.txt

coverage:
	coverage run --branch --source application/ -m pytest tests/
	coverage html --title="Dashboard+ coverage report"
	coverage report -m

cloc:
	pygount --format=cloc-xml --out cloc.xml --suffix=py application/

unit-test:
	rm -r --force .pytest_cache
	pytest tests/
