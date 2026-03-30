# pyflowkit

## Описание

Весь процесс:

- сделаена структура пакета
- написан тест
- собран пакет
- выложен в TestPyPI
- настроен Makefile

---

## Что делает пакет?

Пока в пакете есть простой пример:

- функция `hello()` в `core.py`

---

## Структура проекта

- src/pyflowkit/
    init.py
    core.py

- tests/
    test_pyflowkit.py

- pyproject.toml
- Makefile
- README.md

---

## Установка из TestPyPI

pip install --index-url https://test.pypi.org/simple/ pyflowkit

## Пример использования

from pyflowkit.core import hello
hello()

## Как запускать без Make?
1. создаем окружение
python3 -m venv .venv
source .venv/bin/activate
2. устанавливаем зависимости: 
python -m pip install -U pip setuptools wheel build pytest
3. запускаем тесты:
pytest -v
4. собираем пакет:
python -m build

## Использование Makefile
make install   # установить зависимости
make test      # запустить тесты
make build     # собрать пакет
make clean     # очистить проект
make check     # проверка

## Требования

Python 3.10+
pip

## Ссылки

- TestPyPI:
https://test.pypi.org/project/pyflowkit/0.1.0

- GitHub:
https://github.com/ccccxxip/semenova_fossdev/tree/feature/testpypi-package