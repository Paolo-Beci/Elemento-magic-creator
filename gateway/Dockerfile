FROM golang:latest AS builder

WORKDIR /app

COPY . .

RUN cd src/gateway && go build -o /app/bin/gateway

FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/bin/gateway .

EXPOSE 8080

CMD ["/app/bin/gateway"]
