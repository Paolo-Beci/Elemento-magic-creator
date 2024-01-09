FROM golang:latest AS builder

WORKDIR /app

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN cd src/gateway && go build -o /app/bin/gateway

FROM alpine:latest
RUN apk add ca-certificates

COPY --from=builder /app/bin/gateway .

EXPOSE 8080

CMD ["/app/bin/gateway"]
