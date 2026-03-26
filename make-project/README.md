В проекте используется Makefile как единая точка входа

установка зависимостей:
make install

запуск:
make run

проверить типы:
make typecheck

проверить зависимостей:
make check-requirements

все проверки:
make check

Все команды используют .venv/bin, поэтому не нужно активировать окружение.