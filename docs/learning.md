# Learning Plan for Junior Developer

## Основы проекта и тулинга

### 1: Знакомство с проектом

- [ ] Клонировать репозиторий
- [ ] Установить `uv`
- [ ] Запустить `make install` и `make check`
- [ ] Изучить структуру проекта
- [ ] Прочитать `pyproject.toml` — понять, что там настроено

### 2: uv и зависимости

- [ ] Изучить команды `uv`: `run`, `sync`, `pip install`, `add`, `remove`
- [ ] Добавить новую dev-зависимость через `uv add --dev <pkg>`
- [ ] Понять разницу между `dependencies` и `optional-dependencies`

### 3: ruff — линтер и форматтер

- [ ] Нарочно нарушить правило линтера (например, неиспользуемый импорт)
- [ ] Запустить `make lint` и увидеть ошибку
- [ ] Запустить `make fix` и увидеть исправление
- [ ] Изучить правила: E, F, I, N, W, UP, B, C4, SIM

### 4: mypy — строгая типизация

- [ ] Написать функцию без type hints
- [ ] Запустить `make typecheck` и увидеть ошибку
- [ ] Добавить type hints
- [ ] Понять разницу `str | None` vs `Optional[str]`

### 5: pytest — тестирование

- [ ] Написать свой первый тест в `tests/test_mine.py`
- [ ] Использовать паттерн Arrange-Act-Assert
- [ ] Запустить `make test`
- [ ] Попробовать `pytest.mark.parametrize`

## Ключевые принципы

1. **Весь код с type hints** — mypy strict не простит
2. **Всё через uv** — не устанавливай pip-пакеты глобально
3. **Прежде чем push — make check** — lint + typecheck + test
4. **Arrange-Act-Assert** — паттерн для тестов
5. **Google docstrings** — для всего публичного API

## Чеклист перед каждым коммитом

```bash
make check
```

Если зелёное — можно коммитить. 🔒
