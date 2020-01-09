FROM python:3.8-alpine as build

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

COPY ./api/requirement.txt requirement.txt

RUN  apk add gcc mariadb-dev python3-dev build-base libffi-dev g++ libc-dev linux-headers &&\
pip install  -r requirement.txt 

COPY ./api /api
WORKDIR /api


CMD ["sh","-c","python manage.py runserver 0.0.0.0:8000"]