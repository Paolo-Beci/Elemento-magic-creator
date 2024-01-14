FROM ubuntu:latest

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip

EXPOSE 1113
RUN mkdir /web_scraper/
WORKDIR /web_scraper/

COPY ./ ./

RUN python3 -m pip install --no-cache-dir -U -r ./requirements.txt
RUN playwright install
RUN playwright install-deps

ENTRYPOINT python3 web_scraper.py
