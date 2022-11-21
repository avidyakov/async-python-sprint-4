FROM python:3.11.0

EXPOSE 8000

WORKDIR /app

RUN pip install poetry && poetry config virtualenvs.create false && pip install pydantic[dotenv]

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-interaction --no-ansi --no-cache

COPY . /app

CMD ["python", "src/main.py"]
