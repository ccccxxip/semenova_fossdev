.PHONY: help test clean install run

help:
	@echo "Available targets:"
	@echo "  make test    - Run tests"
	@echo "  make clean   - Clean temporary files"
	@echo "  make install - Install dependencies"
	@echo "  make run     - Run order_service on port 8803 (requires product_service on port 8001)"

test:
	pytest tests/ -v

clean:
	rm -rf __pycache__ .pytest_cache build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

install:
	poetry install --no-root

run:
	PRODUCT_SERVICE_URL=http://127.0.0.1:8001 poetry run uvicorn src.app.main:app --reload --host 127.0.0.1 --port 8803
