FROM python:3.8

RUN pip install 'poetry==1.3.1'

WORKDIR /application
COPY requirements.txt /application/

RUN pip install -r requirements.txt

COPY app.py /application/app.py
