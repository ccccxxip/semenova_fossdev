.PHONY: help test clean install create-structure

help:
	@echo "Available targets:"
	@echo "  make test           - Run tests"
	@echo "  make clean          - Clean temporary files"
	@echo "  make install        - Install dependencies"
	@echo "  make create-structure - Create full project structure"

test:
	pytest tests/

clean:
	rm -rf __pycache__ .pytest_cache build dist *.egg-info

install:
	pip install -e .

create-structure:
	@echo "Creating structure for $(PRACTICE)"
	mkdir -p src tests docs
	touch src/.gitkeep
	touch tests/.gitkeep
	echo "# $(PRACTICE)" > README.md
	echo "# Domain documentation for $(PRACTICE)" > docs/DOMAIN.md
	printf "requests\npytest\n" > requirements.txt
	printf "from setuptools import setup, find_packages\n\nsetup(\n    name=\"$(PRACTICE)\",\n    version=\"0.1.0\",\n    packages=find_packages(),\n    install_requires=[\"requests\"],\n    author=\"Your Name\",\n    description=\"A simple $(PRACTICE) implementation\",\n)\n" > setup.py
	@echo "Structure created successfully"
