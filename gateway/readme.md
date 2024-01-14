# Gateway
Questo servizio si occupa di gestire l'interfaccia tra l'utente e i servizi sul server. Viene fatto un controllo sulla correttezza del payload e viene inoltrato al servizio midlleware. Espone la porta 8080, che è l'unica porta accessibile dall'esterno.

## APIs
- /api/v1/specs/{payload}
    - **GET**: Restituisce la configurazione del servizio indicato nel campo `payload` sotto forma di un JSON compatibile con i servizi di Elemento Cloud.

## Setup
*Last update: 12/01/2024*

Tramite Docker-compose e Dockerfile.

## Dependencies
- [Gorilla mux](https://github.com/gorilla/mux)
- [Gorilla handlers](https://github.com/gorilla/handlers)