FROM python:3.7.7-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ['uwsgi', 'app.ini' ]