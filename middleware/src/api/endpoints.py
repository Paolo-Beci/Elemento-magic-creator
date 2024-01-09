# api/endpoints.py
from flask import request, jsonify

def register_endpoints(app, get_services, save_service, get_service):
    @app.route('/api/v1/get-specs', methods=['GET'])
    def get_specs():
        name_param = request.args.get('name')

        print(request.headers)
        print(f"Service name ricevuto da gateway: {name_param}")

        # Verifica se il servizio esiste
        service = get_service(name_param)
        if service:
            # Servizio esiste, esegui la tua logica
            return service
        else:
            # Servizio non esiste
            return jsonify({'error': 'Servizio non trovato'}), 404
