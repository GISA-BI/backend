FROM python:3.13-alpine

COPY ./requirements.txt /tmp

WORKDIR /tmp

RUN pip install -r requirements.txt
