FROM python:3.10-slim

LABEL org.opencontainers.image.source="https://github.com/"

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends --yes \
    netcat \
    libpq-dev gcc python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry gunicorn gevent

WORKDIR /app
COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY .docker/app/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 8000
ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["gunicorn", "--bind", ":8000", "--graceful-timeout=900", "--timeout=900", "--workers", "3", "--error-logfile", "-", "--access-logfile", "-", "app.wsgi:application"]