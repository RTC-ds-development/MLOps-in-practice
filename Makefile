install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C basic_example.py

test:
	python -m pytest -vv --cov=basic_operations test_basic_operations.py

format:
	black *.py