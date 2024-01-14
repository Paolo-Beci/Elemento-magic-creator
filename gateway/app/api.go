package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"regexp"
	"time"

	"github.com/gorilla/handlers"
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
	remoteHost string
	remotePort string
	client     *http.Client
}

func Gateway(listenAddr, remoteHost, remotePort string) *APIServer {
	return &APIServer{
		listenAddr: listenAddr,
		remoteHost: remoteHost,
		remotePort: remotePort,
		client: &http.Client{
			Timeout: 500 * time.Second, 
		},
	}
}

// Routes Initialization
func (s *APIServer) Run() {
	router := mux.NewRouter()

	// Enable CORS middleware
    corsMiddleware := handlers.CORS(
        handlers.AllowedOrigins([]string{"*"}), // DA MODIFICARE con indirizzo specifico
        handlers.AllowedMethods([]string{"GET"}),
        handlers.AllowedHeaders([]string{"Content-Type", "Authorization"}),
    )
	router.Use(corsMiddleware)

	router.HandleFunc("/api/v1/specs/{payload}", makeHTTPHandleFunc(s.handleGetSpecsCall))

	log.Println("Starting API server on port", s.listenAddr)

	http.ListenAndServe(s.listenAddr, router)
}

// API Routes

// GET /api/v1/specs/{payload}
// Returns the specs of the given payload.
// Params: payload (string) is the name of the service to get the specs of.
func (s *APIServer) handleGetSpecsCall(w http.ResponseWriter, r *http.Request) error {
	payload := mux.Vars(r)["payload"]
	
	// Payload validation
	matched, err := regexp.MatchString(`^[a-zA-Z0-9\s]+$`, payload)
	if err != nil || !matched {
		return WriteJSON(w, http.StatusBadRequest, apiError{Error: "Invalid payload format"})
	}

	encodedPayload := url.Values{"name": {payload}}.Encode()

	// Make a GET request to Middleware container
	remoteURL := fmt.Sprintf("http://%s:%s/api/v1/get-specs?%s", s.remoteHost, s.remotePort, encodedPayload)
	response, err := s.client.Get(remoteURL)
	if err != nil {
		fmt.Println("Error making GET request to another container:", err)
		return WriteJSON(w, http.StatusInternalServerError, apiError{Error: "Internal Server Error"})
	}

	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		fmt.Println("Error reading response body:", err)
		return WriteJSON(w, http.StatusInternalServerError, apiError{Error: "Internal Server Error"})
	}
	
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(response.StatusCode)
	_, err = w.Write(body)
	return err
}
