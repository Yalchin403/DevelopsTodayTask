FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2==2.8.6 \
    && pip install -U django-rest-knox
RUN pip install -r /requirements.txt
RUN mkdir /app
COPY . /app
WORKDIR /app