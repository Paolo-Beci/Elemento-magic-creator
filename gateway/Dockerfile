FROM golang:1.22-rc-alpine

RUN mkdir /app
ADD . ./app
WORKDIR /app

COPY go.* ./
RUN go mod download

RUN go build -o gateway .

EXPOSE 8080

CMD ["/app/gateway"]