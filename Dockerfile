FROM python:3.8-slim-buster

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .


RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
