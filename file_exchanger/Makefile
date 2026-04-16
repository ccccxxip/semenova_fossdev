.PHONY: help test clean install

help:
	@echo "Available targets:"
	@echo "  make test    - Run tests"
	@echo "  make clean   - Clean temporary files"
	@echo "  make install - Install dependencies"

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
	cat > setup.py << 'SETUP'
from setuptools import setup, find_packages

setup(
    name="$(PRACTICE)",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Your Name",
    description="A simple $(PRACTICE) implementation",
)
SETUP
	@echo "Structure created successfully"
