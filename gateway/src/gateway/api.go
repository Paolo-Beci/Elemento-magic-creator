package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"


	"github.com/gorilla/mux"
)

// Packages used:
// Gorilla mux licence - https://github.com/gorilla/mux#BSD-3-Clause-1-ov-file

func WriteJSON(w http.ResponseWriter, status int, v any) error {
	w.WriteHeader(status)
	w.Header().Set("Content-Type", "application/json")
	return json.NewEncoder(w).Encode(v)
}

type apiFunc func(w http.ResponseWriter, r *http.Request) error

type apiError struct {
	Error string
}

func makeHTTPHandleFunc(f apiFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		err := f(w, r)
		if err != nil {
			fmt.Println("Error handling request:", err)
			WriteJSON(w, http.StatusBadRequest, apiError{Error: err.Error()})
		} 
	}
}

type APIServer struct {
	listenAddr string
	remoteHost  string 
	remotePort  string // DA TOGLIERE SE FUNZIONA IL NETWORKING
	client      *http.Client
}

func Gateway(listenAddr, remoteHost, remotePort string) *APIServer {
	return &APIServer{
		listenAddr: listenAddr,
		remoteHost: remoteHost,
		remotePort: remotePort,
		client: &http.Client{
			Timeout: 5 * time.Second, // Set a timeout for the HTTP client
		},
	}
}

// Routes Initialization 
func (s *APIServer) Run() {
	router := mux.NewRouter()

	router.HandleFunc("/api/v1/specs/{payload}", makeHTTPHandleFunc(s.handleGetSpecsCall))

	log.Println("Starting API server on port", s.listenAddr)

	http.ListenAndServe(s.listenAddr, router)
}

// API Routes
func (s *APIServer) handleGetSpecsCall(w http.ResponseWriter, r *http.Request) error {
	specs := NewSpecs("Test GET response")

	payload := mux.Vars(r)["payload"]
	fmt.Println("Payload:", payload)

	// Make a GET request to middleware container
	remoteURL := fmt.Sprintf("http://%s:%s/api/v1/get-specs?name=%s", s.remoteHost, s.remotePort, payload) // DA TOGLIERE PORTA SE FUNZIONA IL NETWORKING
	response, err := s.client.Get(remoteURL)
	if err != nil {
		fmt.Println("Error making GET request to another container:", err)
		return WriteJSON(w, http.StatusInternalServerError, apiError{Error: "Internal Server Error"})
	}
	defer response.Body.Close()

	return WriteJSON(w, http.StatusOK, specs)
}