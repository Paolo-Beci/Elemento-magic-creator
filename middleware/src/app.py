# main.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from api.endpoints import register_endpoints

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'  # Database SQLite

db = SQLAlchemy(app)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(255), unique=True, nullable=False)
    json_data = db.Column(db.JSON, nullable=False)

def get_services():
    services = Service.query.all()
    services_list = []

    for service in services:
        services_list.append({'service_name': service.service_name, 'json_data': service.json_data})

    return jsonify({'services': services_list})

def save_service():
    data = request.get_json()
    service_name = data.get('service_name')
    json_data = data.get('json_data')

    if not service_name or not json_data:
        return jsonify({'error': 'Nome del servizio o dati mancanti'}), 400
    
    new_service = Service(service_name=service_name, json_data=json_data)
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'message': 'Servizio salvato con successo'})

def get_service(service_name):
    service = Service.query.filter_by(service_name=service_name).first()

    if service:
        return jsonify({'service_name': service.service_name, 'json_data': service.json_data})
    else:
        return None
    
register_endpoints(app ,get_services, save_service, get_service)

if __name__ == "__main__":
    app.run(port=5001, debug=True)


