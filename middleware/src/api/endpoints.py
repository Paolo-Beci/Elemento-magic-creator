# api/endpoints.py
from flask import request, jsonify

def register_endpoints(app):
    @app.route('/api/v1/get-specs', methods=['GET'])
    def get_specs():
        name_param = request.args.get('name')

        print(request.headers)
        print(f"Parametro GET 'name': {name_param}")

        return jsonify({'message': f'Hello {name_param} from the middleware!'})
