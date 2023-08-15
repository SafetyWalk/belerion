FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /safewalk
WORKDIR /safewalk
ADD . /safewalk/
RUN pip install -r requirements.txt