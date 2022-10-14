FROM python:3.8-slim-buster

ENV DockerHOME=/home/app/web
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

COPY . .

RUN pip install --upgrade pip && pip install -r requirements/production.txt

EXPOSE 8000
