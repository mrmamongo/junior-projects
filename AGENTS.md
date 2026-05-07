# Правила работы агента с проектом

> Этот файл создан для OpenCode. Агент читает его при старте сессии.

## Стек проекта

- **Python** 3.11+
- **uv** — package manager и виртуальное окружение
- **ruff** — lint + format
- **mypy** — strict type checking
- **pytest** — тестирование

## Структура директорий

```
src/project_name/    — исходный код (Python пакет)
tests/               — тесты (pytest)
docs/                — документация и планы обучения
.pyproject.toml      — зависимости и конфигурация инструментов
Makefile             — команды разработки
```

## Код-стиль

- Весь код с **type hints**
- **Google-style docstrings** для публичного API
- **Arrange-Act-Assert** паттерн для тестов
- Максимальная длина строки: **88 символов**
- Python 3.11+ фичи: `match/case`, `str | None`, etc.

## Команды разработки

```bash
make install    # установка зависимостей
make test       # pytest
make lint       # ruff linter
make format     # проверка форматирования
make typecheck  # mypy strict
make check      # всё вместе: lint + typecheck + test
```

## Ограничения агента

- **read-only режим** — агент читает код, но не редактирует файлы
- Агент может объяснять, советовать, показывать примеры
- Код пишет **только junior** — агент лишь направляет

## Процесс работы

1. Запустить `make check` перед каждым коммитом
2. Все тесты должны проходить
3. mypy strict — без ошибок
4. ruff — без предупреждений

## Конфигурация OpenCode

- Агент: `.opencode/agents/mentor.md`
- Конфиг: `.opencode/opencode.json`
- Инструкции: `.opencode/instructions.md`
