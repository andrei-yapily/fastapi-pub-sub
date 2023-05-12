FROM python:3.8

WORKDIR /application

COPY requirements.txt /application/

RUN pip install -r requirements.txt


COPY models.py /application/models.py
COPY app.py /application/app.py