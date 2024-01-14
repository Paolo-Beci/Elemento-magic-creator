# api/endpoints.py
from flask import request, jsonify
from utils.helpers import webscraper, ollama


def register_endpoints(app, get_services, save_service, get_service):
    @app.route('/api/v1/get-specs', methods=['GET'])
    def get_specs():
        name_param = request.args.get('name')
        
        website = webscraper(name_param)
        
        component_response = ollama(website)
        if component_response:
            # save_service(component_response['service_name'], component_response['json_data'])
            return jsonify({'message': component_response})

        return jsonify({'error': 'Servizio non trovato e impossibile ottenere i dati dal componente'}), 404

    
    @app.route('/api/v1/get-services', methods=['GET'])
    def get_all_services():
        return get_services()