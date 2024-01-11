# utils/helpers.py
import requests

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