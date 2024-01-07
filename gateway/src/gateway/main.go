package main

func main() {
	server := Gateway(":8080")
	server.Run()
}