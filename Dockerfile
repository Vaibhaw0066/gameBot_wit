FROM python:3.8-slim-buster

ADD . /gamebot

WORKDIR /gamebot
RUN apt-get update && apt-get install -y python3-setuptools
RUN pip install -r requirements.txt


EXPOSE 5000
CMD [ "gunicorn", "-w", "2", "--threads=2", "--log-level", "debug", "chatbot:app", "--bind", "0.0.0.0:5000" ]
