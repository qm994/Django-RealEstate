# resource: https://docs.docker.com/compose/django/
FROM python:3.8-slim-buster
LABEL maintainer qm28@georgetown.edu

# So the logs can always write to container logs and not get buffered at first place
ENV PYTHONUNBUFFERED 1

COPY ./requiremnets.txt /requiremnets.txt
RUN pip install -r /requiremnets.txt

RUN mkdir /app
WORKDIR /app
COPY . /app/
