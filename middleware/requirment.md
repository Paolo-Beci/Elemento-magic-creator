# Requisiti del Middleware

Il middleware deve svolgere il ruolo di intermediario tra un API Gateway e vari componenti del sistema. Di seguito sono elencati i requisiti principali del middleware:

## Funzionalità Principali

1. Accettazione delle API in Ingresso:
Il middleware deve essere in grado di accettare richieste API in ingresso provenienti dall'API Gateway.
2. Risposta alle Richieste GET:
Gestire richieste GET inviate dall'API Gateway e prendere decisioni sulla base di queste richieste.
3. Verifica Presenza Programma nel Database Interno:
Verificare se il programma richiesto è presente nel database interno.
4. Gestione delle Comunicazioni tra Componenti:
Coordinare e gestire le comunicazioni tra il database interno, il web scraper e altri componenti del sistema.
5. Utilizzo del Web Scraper:
Se il programma richiesto non è presente nel database, utilizzare il web scraper per cercare i requisiti su Internet.
6. Elaborazione HTML da Web Scraper:
Ricevere l'HTML del sito web ottenuto dal web scraper e passarlo al componente "ollama" per l'elaborazione.
7. Risposta in Formato JSON:
Convertire il risultato ottenuto dal componente "ollama" in un formato JSON.
8. Invio della Risposta al Mittente Originale:
Inviare la risposta in formato JSON all'API Gateway che ha originariamente inviato la richiesta GET.
## Integrazione con Altri Componenti

-  Comunicazione con il Database Interno:
Stabilire una connessione e comunicare con il database interno per le operazioni di verifica della presenza del programma.
- Coordinazione con il Web Scraper:
Integrazione con il web scraper per inoltrare richieste di ricerca e ricevere l'HTML del sito web.
- Chiamata al Componente "ollama":
Inoltrare l'HTML del sito web al componente "ollama" e ricevere il risultato elaborato in formato JSON.
## Sicurezza e Robustezza

- Gestione degli Errori:
Implementare un sistema di gestione degli errori per affrontare eventuali fallimenti durante le operazioni di comunicazione con i componenti e durante il processo di scraping.
- Validazione delle Richieste:
Validare le richieste in ingresso per garantire la sicurezza e la conformità ai formati attesi.
- Protezione contro Attacchi:
Implementare misure di sicurezza per proteggere il middleware da potenziali attacchi esterni.
## Documentazione

- Documentazione API:
Creare una documentazione chiara e completa per le API esposte dal middleware.
- Guida per lo Sviluppatore:
Fornire una guida per gli sviluppatori che spieghi come installare, configurare e estendere il middleware.
## Requisiti Tecnici

- Linguaggio di Programmazione:
Il middleware deve essere implementato utilizzando il linguaggio di programmazione Python.
- Containerization:
Il middleware deve essere containerizzato utilizzando Docker per semplificare il deployment.
- Comunicazione Asincrona:
Implementare la comunicazione asincrona, se necessario, per gestire le chiamate tra i componenti in modo efficiente.
