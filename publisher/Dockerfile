FROM python:3.8

RUN pip install 'poetry==1.3.1'

WORKDIR /application
COPY poetry.lock pyproject.toml /application/

RUN poetry install

COPY models.py /application/models.py
COPY app.py /application/app.py