FROM python:3

RUN mkdir /code

WORKDIR /code

RUN pip install wheel
RUN pip install django
RUN pip install django-filter
RUN pip install django-graphql-jwt

COPY . /code/
