FROM python:3

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    build-essential

COPY . /app/

RUN python -m venv /env

ENV PATH="/env/bin/:$PATH"

COPY entrypoint.sh /app/entrypoint.sh

RUN python -m  pip install --upgrade pip

COPY  requirements.txt /app/

RUN pip install --default-timeout=100 -r requirements.txt
