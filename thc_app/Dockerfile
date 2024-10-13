FROM python:3.11-slim

WORKDIR /thc_app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get install -y libpq-dev  # If using PostgreSQL

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]


