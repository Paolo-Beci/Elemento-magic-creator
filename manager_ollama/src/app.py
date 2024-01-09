from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

structure = """{
    "slots": ,
    "overprovision": ,
    "allowSMT": ,
    "archs": ,
    "flags": ,
    "min_frequency": ,
    "ramsize": ,
    "reqECC": ,
    "misc": {"os_family": "", "os_flavour": ""},
    "pci": [
        {
            "vendor": "",
            "model": "",
            "quantity": 
        },
        {
            "vendor": "",
            "model": "",
            "quantity": 
        }
    ]
}"""

template = """
### Example of json files

*vmspec.json*
| Name | datatype | Brief description | 
| ---- |----------| ------------------|
| slots | int | number of cores |
| overprovision | int | maximum VMs for each core |
| allowSMT | bool | |
| archs | string | architecture of the system |
| flags | list | processor's instruction set architecture |
| min_frequency | float | minimum processor frequency expressed in GHz |
| ramsize | int Bytes | RAM dimension expressed in Bytes |
| reqECC | bool | request for ECC RAM |
| misc | dictionary | OS Infos |
| pci | list of dictionary | Graphic card specs:<br>- vendor code <br> - model code <br> - quantity <br><br> Audio card specs: <br>- vendor code <br> - model code <br> - quantity <br><br> *NB: You can mount a spare audio card but not a spare graphic card, every graphic card has to be mounted along with its related audio card*|   <pre lang=json>"pci": [<br>    {<br>        "vendor": "10de", <br>        "model": "24b0", <br>        "quantity": 1 <br>    },<br>    { <br>        "vendor": "10de",<br>        "model": "228b", <br>        "quantity": 1<br>    }<br>]</pre>
"""

@app.route('/manager-ollama/check-server', methods=['GET'])
def check_server():
    return jsonify({'message': 'Manager-ollama server is running'})

# Payload sample: manager-ollama/payload?name=adobe
@app.route('/manager-ollama/payload', methods=['GET'])
def ollama_request():
    try:
        # Extract the JSON data from the request body
        request_data = request.json

        # Check if 'prompt' is present in the request data
        if 'data' in request_data:
            api_url = 'http://localhost:11434/api/generate'

            #First step: refinement of the requirement body
            data = request_data['data']
            prompt = "Get all information about techinical System Requirements from this text: " + data

            # Construct the payload using the extracted prompt
            payload = {
                "model": "llama2",
                "prompt": prompt,
                "stream": False
            }

            response = requests.post(api_url, json=payload)

            #Second step: generate the actual json
            if response.status_code != 200:
                return jsonify({'error': 'Failed to fetch data from Ollama API #1'}), response.status_code
            
            data  = response.json()
            if 'response' not in data:
                return jsonify({'error': 'Failed to fetch data from Ollama API #2'}), 400
            
            requirement = data['response']
            prompt = "Considering the requirements: "+ requirement +" Create a JSON following rules: "+ template +" and return only the json with this structure (not other text): " + structure

            # Construct the payload using the extracted prompt
            payload = {
                "model": "llama2",
                "prompt": prompt,
                "stream": False
            }

            response = requests.post(api_url, json=payload)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                result = response.json()
                return jsonify(result['response'])
            else:
                return jsonify({'error': 'Failed to fetch data from Ollama API #2'}), response.status_code
        else:
            return jsonify({'error': 'data not found in the request body'}), 400

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request to Ollama API failed: {e}'}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
