# api/endpoints.py
from flask import request, jsonify
import requests

def register_endpoints(app, get_services, save_service, get_service):
    @app.route('/api/v1/get-specs', methods=['GET'])
    def get_specs():
        name_param = request.args.get('name')

        print(request.headers)
        print(f"Service name ricevuto da gateway: {name_param}")

        service = get_service(name_param)
        if service:
            return service
        else:
            website = webscraper(name_param)
            component_response = ollama(website)

            if component_response:
                save_service(component_response['service_name'], component_response['json_data'])
                return jsonify({'message': 'Servizio salvato con successo'})

            return jsonify({'error': 'Servizio non trovato e impossibile ottenere i dati dal componente'}), 404

    def webscraper(service_name):
        component_url = f'http://localhost:5001/api/v1/get-component'
        response = requests.get(component_url, params={'name': service_name})

        if response.status_code == 200:
            return response.json()

        # Altrimenti, restituisci None
        return None
    
    def ollama(website):
        component_url = f'http://localhost:5002/api/v1/get-specs'
        response = requests.get(component_url, params={'website': website})

        if response.status_code == 200:
            return response.json()

        # Altrimenti, restituisci None
        return None