# Python Project Skeleton

Skeleton проекта для обучения junior-разработчика современному Python-стеку.

---

## Требования

- **Python** `3.11+`
- **uv** — ультрабыстрый package manager и инструмент для работы с виртуальными окружениями

---

## Установка `uv`

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Подробнее: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

---

## Быстрый старт

```bash
# 1. Клонировать репозиторий
git clone <repo-url>
cd project_name

# 2. Установить зависимости
make install

# 3. Запустить полную проверку
make check

# 4. Запустить тесты
make test
```

---

## Структура проекта

```
project_name/
├── .python-version          # Указывает Python 3.11
├── README.md                # Этот файл
├── pyproject.toml           # Конфигурация проекта, зависимостей, инструментов
├── Makefile                 # Команды для разработки
├── .github/workflows/ci.yml # GitHub Actions CI pipeline
│
├── src/
│   └── project_name/        # Исходный код проекта
│       ├── __init__.py      # Точка входа, __version__
│       └── ...
│
├── tests/                   # Тесты
│   ├── __init__.py
│   └── test_example.py      # Пример теста с pytest
│
├── docs/
│   └── learning.md          # План обучения junior-разработчика
│
└── .opencode/               # Инструкции и конфиги для AI-агента
    ├── instructions.md      # Как агент должен работать с проектом
    └── tools.json           # Доступные агенту инструменты
```

---

## Доступные команды `make`

| Команда       | Описание                                          |
|---------------|---------------------------------------------------|
| `make install`| Установить зависимости через `uv`                 |
| `make sync`   | Синхронизировать lockfile                         |
| `make test`   | Запустить тесты через `pytest`                    |
| `make lint`   | Проверить код линтером `ruff`                     |
| `make format` | Проверить форматирование через `ruff`             |
| `make fix`    | Автоисправить проблемы линтера и форматирования   |
| `make typecheck` | Запустить `mypy` в strict mode                 |
| `make check`  | Полная проверка: lint + format + typecheck + test |
| `make clean`  | Удалить артефакты сборки и кэш                    |

---

## Тулинг

### `uv`
- Управление зависимостями и виртуальное окружение
- Команды: `uv pip install`, `uv run`, `uv sync`

### `ruff`
- Линтер и форматтер, заменяет `flake8`, `black`, `isort`
- Правила: E, F, I, N, W, UP, B, C4, SIM
- Google-style docstrings через `pydocstyle`

### `mypy`
- Строгая статическая проверка типов (`strict = true`)
- Все импорты должны иметь типизацию (`ignore_missing_imports = false`)

### `pytest`
- Фреймворк для тестирования
- Директория `tests/`, файлы `test_*.py`

---

## Работа с AI-агентом (OpenCode)

В директории `.opencode/` находятся инструкции и конфигурация для AI-агента.

Агент знает:
- Где исходный код (`src/project_name/`)
- Где тесты (`tests/`)
- Какие инструменты используются (`uv`, `ruff`, `mypy`, `pytest`)
- Как должен помогать junior-разработчику

Смотри `.opencode/instructions.md` для деталей.

---

## Обучение

План обучения для junior-разработчика находится в `docs/learning.md`.

