PYTHON = .venv/bin/python
PIP = .venv/bin/pip

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) src/app.py

typecheck:
    $(PYTHON) -m mypy src/ --ignore-missing-imports

format:
	$(PYTHON) -m black src/

check-requirements:
	$(PYTHON) scripts/check_requirements.py


check: typecheck check-requirements