package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

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
}

func Gateway(listenAddr string) *APIServer {
	return &APIServer{
		listenAddr: listenAddr,
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

	name := mux.Vars(r)["payload"]
	fmt.Println("Payload:", name)

	return WriteJSON(w, http.StatusOK, specs)
}
