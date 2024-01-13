FROM golang:1.22-rc-alpine

WORKDIR /app

COPY ./app /app
COPY go.* /app
RUN go mod download

RUN go build -o gateway .

EXPOSE 8080

CMD ["./gateway"]    