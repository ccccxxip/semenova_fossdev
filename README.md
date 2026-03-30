# pyflowkit

- упаковки проектов (packaging)
- тестирования (pytest)
- сборки и публикации пакетов в TestPyPI

## Структура

- src/ 
pyflowkit/
init.py
core.py

- tests/
test_pyflowkit.py

- pyproject.toml
- Makefile


## Что может делать

- Тест с помощью pytest
- Сборка через build
- команды в Makefile
- опубликовать в TestPyPI


## Установка
python3 -m venv .venv
source .venv/bin/activate
make install

## Запуск тестов
make test
или 
pytest -v

## Сборка
make build

## Установка из TestPyPI
pip install -i https://test.pypi.org/simple/ pyflowkit

## Требования
- Python 3.10+
- pip
- pytest
- build
- setuptools