FROM python:3.9-slim

WORKDIR /manager_ollama/app

COPY . /manager_ollama/app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV FLASK_APP=app.py

CMD ["flask", "run"]