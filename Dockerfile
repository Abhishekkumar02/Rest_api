FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD . /code/

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y default-mysql-client && rm -rf /var/lib/apt

COPY . /code/
