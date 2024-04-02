FROM python:3.10.5-alpine

LABEL maintainer="brikocorp@gmail.com"

RUN mkdir "app"
WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000