# resource: https://docs.docker.com/compose/django/
FROM python:3
LABEL maintainer qm28@georgetown.edu

#Prevents Python from writing pyc files to disc (equivalent to python -B option)#
ENV PYTHONDONTWRITEBYTECODE 1
# So the logs can always write to container logs and not get buffered at first place
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code 
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get remove -y libpq5
RUN apt-get install -y python-dev python3-dev
RUN apt-get install -y libpq-dev

RUN pip install -r requirements.txt
COPY . /code/

