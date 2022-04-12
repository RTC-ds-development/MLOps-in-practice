install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C basic_example.py

format:
	black *.py

test:
	python -m pytest test_basic_operations.py