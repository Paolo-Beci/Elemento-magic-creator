FROM python:3.9-alpine

WORKDIR /middleware

COPY src/requirements.txt /middleware/
COPY dummy_script.sh /middleware/

RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && chmod +x dummy_script.sh

CMD ["/middleware/dummy_script.sh"]
