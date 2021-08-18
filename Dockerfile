FROM python:3.8
ENV PYTHONBUFFERED 1
RUN mkdir /django_crud
WORKDIR /django_crud
ADD . /django_crud/
RUN pip install -r requirements.txt
