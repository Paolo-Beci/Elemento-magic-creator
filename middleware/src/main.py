# main.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from api.endpoints import register_endpoints

app = Flask(__name__)

register_endpoints(app)

if __name__ == "__main__":
    app.run(debug=True)
