FROM python:3.8-alpine as build

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

COPY requirements.txt requirements.txt

RUN apk update &&\
    apk add gcc mariadb-dev python3-dev build-base libffi-dev g++ libc-dev linux-headers &&\
    pip install  -r requirements.txt

COPY ./api /api
WORKDIR /api


CMD ["sh","-c","gunicorn  --bind 0.0.0.0:$PORT projects.wsgi:application"]

