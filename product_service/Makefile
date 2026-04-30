.PHONY: help test clean install run

help:
	@echo "Available targets:"
	@echo "  make test    - Run tests"
	@echo "  make clean   - Clean temporary files"
	@echo "  make install - Install dependencies"
	@echo "  make run     - Run product_service on port 8001"

test:
	pytest tests/ -v

clean:
	rm -rf __pycache__ .pytest_cache build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

install:
	poetry install --no-root

run:
	poetry run uvicorn src.main:app --reload --host 127.0.0.1 --port 8001
