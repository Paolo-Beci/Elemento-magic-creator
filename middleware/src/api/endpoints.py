# api/endpoints.py
import time
from flask import request, jsonify
from utils.helpers import webscraper, ollama


def register_endpoints(app, get_services, save_service, get_service):
    @app.route('/api/v1/get-specs', methods=['GET'])
    def get_specs():
        name_param = request.args.get('name')
        start_time = time.time()

        website = webscraper(name_param)

        execution_time_webscraper = time.time() - start_time
        print(f'Tempo di esecuzione di webscraper: {execution_time_webscraper} secondi')
        start_time = time.time()

        component_response = ollama(website)

        execution_time_ollama = time.time() - start_time
        print(f'Tempo di esecuzione di ollama: {execution_time_ollama} secondi')

        if component_response:
            # save_service(component_response['service_name'], component_response['json_data'])
            return jsonify({'message': component_response})

        return jsonify({'error': 'Servizio non trovato e impossibile ottenere i dati dal componente'}), 404

    
    @app.route('/api/v1/get-services', methods=['GET'])
    def get_all_services():
        return get_services()