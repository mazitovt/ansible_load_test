FROM python:3.8

WORKDIR /demo_app

COPY requirements.txt .

RUN apt-get update
RUN pip install -r requirements.txt

COPY ./app ./app

CMD python3 ./app/main.py
