## Architecture
This implementation aims to automatically generate [Elemento ElectroOS custom configs](https://github.com/Elemento-Modular-Cloud/electros) based on the name of a service, like Adobe Photoshop. By doing so, it creates tailor-made virtual machines that meet the recommended requirements of the specified service.
It works by scraping the internet for official recommended configurations and then processing this information with the Ollama model to create a JSON VM config.
The system is based on a microservice architecture, each service is autonomous and exposes endpoints that executes a specific action, every box is a standalone Docker container.

![Architecture](images/architecture.png)

## API endpoints and pipeline

### 1. GET …:5000/api/v1/get-specs?name={…}

The Gateway forwards the request to the middleware.

### 2. GET web_scraper/payload

The Web scraper responds with the HTML without tags in the body as response.

### 3. GET manager_ollama/payload

The ollama manager takes the HTML → filters it → passes it to Ollama that responds with the json.

### 4. GET ollama:11334/…

Gets the model response, it will be used in the response for the middleware.

### 5. Saving on the DB

The result is saved on a DB in order to save time in the future in case the same request is made.

### 6. Passing the response to the gateway and forwarding to the client

## Team
![Elemento_page-0006](https://github.com/Paolo-Beci/NASA-Space-Apps-2023/assets/71789321/a0a55f09-ed98-4081-9598-ea3a15d4a199)
