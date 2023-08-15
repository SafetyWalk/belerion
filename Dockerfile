FROM python:3.10.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /safewalk
WORKDIR /safewalk
ADD . /safewalk/
RUN pip install -r requirements.txt