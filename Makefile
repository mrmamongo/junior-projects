.PHONY: help install sync test lint format typecheck check ci clean

## Default target when just running `make`
.DEFAULT_GOAL := help

## Show this help message
help:
	@echo "Available commands:"
	@echo "  make install   — install dependencies with uv"
	@echo "  make sync      — sync lockfile with uv"
	@echo "  make test      — run pytest suite"
	@echo "  make lint      — run ruff linter"
	@echo "  make format    — run ruff formatter (check mode)"
	@echo "  make fix       — run ruff formatter + linter with auto-fix"
	@echo "  make typecheck — run mypy strict type checking"
	@echo "  make check     — run lint + typecheck + test (full CI check)"
	@echo "  make ci        — same as check, alias for CI pipelines"
	@echo "  make clean     — remove build artifacts"

## Install dependencies using uv
install:
	uv pip install -e ".[dev]"

## Sync lockfile (if you add uv.lock later)
sync:
	uv sync

## Run pytest test suite
test:
	uv run pytest

## Run ruff linter (checks only, no fixes)
lint:
	uv run ruff check src tests

## Run ruff formatter in check mode
format:
	uv run ruff format --check src tests

## Run ruff linter + formatter with auto-fix
fix:
	uv run ruff check --fix src tests
	uv run ruff format src tests

## Run mypy strict type checking
typecheck:
	uv run mypy src tests

## Full check: lint + typecheck + test
check: lint format typecheck test
	@echo "✅ All checks passed!"

## Alias for CI pipelines
ci: check

## Remove build artifacts
clean:
	rm -rf build/ dist/ *.egg-info/ .mypy_cache/ .pytest_cache/ .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
