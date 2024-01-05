FROM alpine:latest

ENV DUMMY_VARIABLE="Hello, i'm the Web scraper!"

WORKDIR /web_scraper
WORKDIR /web_scraper/app

COPY dummy_script.sh /web_scraper/app/
RUN chmod +x /web_scraper/app/dummy_script.sh

CMD ["/web_scraper/app/dummy_script.sh"]
