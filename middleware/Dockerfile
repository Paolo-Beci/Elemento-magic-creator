FROM alpine:latest

ENV DUMMY_VARIABLE="Hello, i'm the Midlleware!"

WORKDIR /midlleware
WORKDIR /midlleware/app

COPY dummy_script.sh /midlleware/app/
RUN chmod +x /midlleware/app/dummy_script.sh

CMD ["/midlleware/app/dummy_script.sh"]
