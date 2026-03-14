# Payments API (TDD Assignment)

Fake payment API built using FastAPI and pytest.

## Setup

pip install fastapi pytest httpx uvicorn

## Run tests

pytest -v

## Architecture

Routes → Service → Fake Repository

The repository stores data in memory using dictionaries.

## Reflection

This project demonstrates test-driven development (TDD). Tests are written before implementation to define expected behavior. The service layer contains the business logic while routes handle HTTP requests. A fake repository replaces a real database so tests remain fast and isolated. Writing tests first helped ensure validation rules and edge cases were handled correctly, such as invalid payment amounts and refund limits.
