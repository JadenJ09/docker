FROM python:3.11.5-slim

WORKDIR /code

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry install --no-interaction --no-ansi

COPY ./src ./src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
