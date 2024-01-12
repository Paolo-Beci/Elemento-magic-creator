# utils/helpers.py
import requests


def webscraper(service_name):
    # component_url = f'webscraper:5001/api/v1/get-component'
    # response = requests.get(component_url, params={'name': service_name})

    # if response.status_code == 200:
    #     return response.json()

    # return None

    # mock return
    mock_response = {
        "data" : "test"
    }
   
    return mock_response


def ollama(website):
    component_url = 'http://manager-ollama:5001/api/v1/generate'
    response = requests.get(component_url, json=mock_response)

    if response.status_code == 200:
        return response.json()

    return None