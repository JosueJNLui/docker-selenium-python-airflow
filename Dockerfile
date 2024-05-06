FROM python:3.10-slim-buster

RUN mkdir /home/bot

WORKDIR /home/bot

COPY requirements.txt .

RUN pip install -r requirements.txt
