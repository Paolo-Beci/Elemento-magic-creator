package main

func main() {
	server := Gateway(":8080", "middleware", "5001")
	server.Run()
}