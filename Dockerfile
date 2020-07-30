FROM python:3

RUN mkdir /code

WORKDIR /code

RUN pip install wheel
RUN pip install django
RUN pip install django-filter
RUN pip install django-graphql-jwt
RUN pip install djongo
RUN pip install django-environ

COPY . /code/
