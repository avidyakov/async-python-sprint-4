FROM python:3.11

WORKDIR /app

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python", "src/main.py"]
