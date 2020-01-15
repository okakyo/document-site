FROM python:3.8-alpine as build

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

COPY requirements.txt requirements.txt

RUN  apk add gcc mariadb-dev python3-dev build-base libffi-dev g++ libc-dev linux-headers &&\
pip install  -r requirements.txt

COPY ./api /api
WORKDIR /api

EXPOSE 8000

RUN python manage.py migrate

