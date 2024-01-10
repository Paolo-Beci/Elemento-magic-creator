from flask import Flask, jsonify, request
from templates import templates
import requests, json, utils

app = Flask(__name__)


### API ###
@app.route("/manager-ollama/check-server", methods=["GET"])
def check_server():
    return jsonify({"message": "Manager-ollama server is running"})


@app.route("/manager-ollama/payload", methods=["GET"])
def ollama_request():
    api_url = "http://localhost:11434/api/generate"

    try:
        request_data = request.json

        if "data" in request_data:
            # First step: refinement of the body
            filtered_text = utils.get_core_info(request_data["data"])

            prompt = (
                "Get all core information about techinical System Requirements from this text:"
                + filtered_text
            )

            payload = {
                "model": "llama2",
                "prompt": prompt,
                "stream": False,
            }

            response = requests.post(api_url, json=payload)

            # Second step: generate the actual json
            if response.status_code != 200:
                return (
                    jsonify({"error": "Failed to fetch data from Ollama API"}),
                    response.status_code,
                )

            data = response.json()
            if "response" not in data:
                return jsonify({"error": "Incorrect response format from Ollama"}), 500

            prompt = (
                "Considering the requirements:"
                + data["response"]
                + "Create a JSON following rules:"
                + templates.get_rules()
                + "Return only the json with this structure (in pci one single GPU and as optional the audio card):"
                + templates.get_structure()
            )

            payload = {
                "model": "llama2",
                "prompt": prompt,
                "format": "json",
                "stream": False,
            }

            response = requests.post(api_url, json=payload)

            if response.status_code == 200:
                result = response.json()
                return jsonify(json.loads(result["response"]))
            else:
                return (
                    jsonify({"error": "Failed to fetch data from Ollama API"}),
                    response.status_code,
                )

        else:
            return jsonify({"error": "data not found in the request body"}), 400

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request to Ollama API failed: {e}"}), 500


### APP (just for testing purpose - use flask run instead) ###
if __name__ == "__main__":
    app.run(port=8000, debug=True)
