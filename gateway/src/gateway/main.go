package main

func main() {
	server := Gateway(":8080", "middleware", "1111")
	server.Run()
}