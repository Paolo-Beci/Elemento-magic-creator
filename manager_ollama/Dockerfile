FROM alpine:latest

ENV DUMMY_VARIABLE="Hello, i'm the manager of Ollama!"

WORKDIR /manager_ollama
WORKDIR /manager_ollama/app

COPY dummy_script.sh /manager_ollama/app/
RUN chmod +x /manager_ollama/app/dummy_script.sh

CMD ["/manager_ollama/app/dummy_script.sh"]
