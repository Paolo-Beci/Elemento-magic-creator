FROM python:3.9-alpine

WORKDIR /middleware

COPY src /middleware/src
COPY src/requirements.txt /middleware/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "/middleware/src/main.py"]
