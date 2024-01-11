from flask import Flask, jsonify, request
import requests, json
import utils.utils as utils
import utils.ollama_utils as ollama_utils

app = Flask(__name__)


##* APIs *##
@app.route("/api/v1/check-server", methods=["GET"])
def check_server():
    return jsonify({"message": "Manager-ollama server is running"})


@app.route("/api/v1/generate", methods=["GET"])
def ollama_request():
    api_url = "http://ollama:11434/api/generate"

    try:
        request_data = request.json

        if "data" in request_data:
            # * First step: refinement of the body
            filtered_text = utils.get_core_info(request_data["data"])
            payload = ollama_utils.first_payload(filtered_text)
            response = requests.post(api_url, json=payload)

            if response.status_code != 200:
                return (
                    jsonify({"error": "Failed to fetch data from Ollama API"}),
                    response.status_code,
                )

            # * Second step: generate the actual json
            data = response.json()
            if "response" not in data:
                return jsonify({"error": "Incorrect response format from Ollama"}), 500

            payload = ollama_utils.second_payload(data)
            response = requests.post(api_url, json=payload)

            if response.status_code != 200:
                return (
                    jsonify({"error": "Failed to fetch data from Ollama API"}),
                    response.status_code,
                )

            # * Third step: refinement of the json
            result = response.json()
            result = utils.refinement(json.loads(result["response"]))
            return jsonify(result)
        else:
            return jsonify({"error": "data not found in the request body"}), 400

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request to Ollama API failed: {e}"}), 500


##* APP (just for testing purpose - use flask run instead) *##
if __name__ == "__main__":
    app.run(port=5001, debug=True)
