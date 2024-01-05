FROM alpine:latest

ENV DUMMY_VARIABLE="Hello, i'm the gateway!"

WORKDIR /gateway
WORKDIR /gateway/app

COPY dummy_script.sh /gateway/app/
RUN chmod +x /gateway/app/dummy_script.sh

CMD ["/gateway/app/dummy_script.sh"]
