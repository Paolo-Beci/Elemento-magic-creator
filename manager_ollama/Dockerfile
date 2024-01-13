FROM python:3.9-slim

WORKDIR /manager_ollama/app

COPY ./src /manager_ollama/app
COPY requirements.txt /manager_ollama/app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]