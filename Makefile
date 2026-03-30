install:
	python -m pip install -U pip setuptools wheel build pytest

test:
	pytest -v

build:
	python -m build