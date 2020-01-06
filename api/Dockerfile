FROM python:3.8-alpine

WORKDIR /api
COPY requirement.txt /api/requirement.txt

RUN  apk add gcc mariadb-dev python3-dev  g++ libc-dev linux-headers &&\
pip install  -r /api/requirement.txt 

