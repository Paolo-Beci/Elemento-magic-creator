build:
	@cd src/gateway && go build -o ../../bin

run: build
	@cd bin && ./gateway

test:
	@go test -v ./test/...