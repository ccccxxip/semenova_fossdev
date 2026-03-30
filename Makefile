install:
	python -m pip install -U pip setuptools wheel build pytest

test:
	pytest -v

run:
	python -m pyflowkit.core