install:
	python -m pip install -U pip setuptools wheel build pytest

test:
	pytest -v

build:
	python -m build
clean:
	rm -rf dist build *.egg-info
	rm -rf __pycache__
	rm -rf src/**/__pycache__
	rm -rf tests/**/__pycache__
check: test