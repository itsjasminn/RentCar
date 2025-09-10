FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY reqs.txt /app/
RUN pip install --upgrade pip && pip install -r reqs.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "root.wsgi:application", "--bind", "0.0.0.0:8000"]
