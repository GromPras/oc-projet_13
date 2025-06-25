FROM --platform=linux/amd64 python:3.12.4-slim-bookworm

RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN addgroup --system app && adduser --system --group app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV ENVIRONMENT prod
ENV TESTING 0
ENV SENTRY_DSN=$SENTRY_DSN

RUN pip install --upgrade pip

WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY static/ ./static/
COPY entrypoint.sh ./src/entrypoint.sh

RUN chmod +x /usr/src/app/src/entrypoint.sh \
    && chown -R app:app /usr/src/app

USER app

# WORKDIR is redundant but makes it clear we need to run the app from within the src/ directory
WORKDIR /usr/src/app/src
ENTRYPOINT ["./entrypoint.sh"]
