# STEP 1: Install base image. Optimized for Python.
FROM python:3.7-slim-buster

RUN pip install Flask 

ADD . /app
WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]