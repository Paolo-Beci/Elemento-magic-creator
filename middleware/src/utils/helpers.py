# utils/helpers.py
import requests


def webscraper(service_name):
    component_url = f'http://web-scraper:1113/requirements'
    response = requests.get(component_url, params={'application_name': service_name})

    if response.status_code == 200:
        return response.json()

    return None


def ollama(website):
    component_url = 'http://manager-ollama:5001/api/v1/generate'
    
    response = requests.get(component_url, json=website)

    if response.status_code == 200:
        return response.json()

    return None