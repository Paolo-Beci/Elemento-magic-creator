from flask import Flask, jsonify, request
import requests, json
import utils.utils as utils
import utils.ollama_utils as ollama_utils

app = Flask(__name__)


##* APIs *##
@app.route("/api/v1/check-server", methods=["GET"])
def check_server():
    return jsonify({"message": "Manager-ollama server is running"})


@app.route("/api/v1/pull/llama2", methods=["POST"])
def llama_pull():
    api_url = "http://ollama:11434/api/pull"
    name = {
        "name": "llama2",
        "stream": False,
    }

    try:
        response = requests.post(api_url, json=name)
        if response.status_code != 200:
            return (
                jsonify({"error": "Failed to pull Llama2"}),
                response.status_code,
            )
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request to Llama2 API failed: {e}"}), 500


@app.route("/api/v1/generate", methods=["GET"])
def ollama_request():
    api_url = "http://ollama:11434/api/generate"

    try:
        if "data" in request.json:
            data = request.json["data"]

            if "direct" not in request.args:
                # * First step: refinement of the body
                filtered_text = utils.get_core_info(data)
                payload = ollama_utils.extract_requirements(filtered_text)
                response = requests.post(api_url, json=payload)

                if response.status_code != 200:
                    if response.status_code == 404: llama_pull()
                    return (
                        jsonify({"error": "Failed to fetch data from Ollama API"}),
                        response.status_code,
                    )

                data = response.json()["response"]

            # * Second step: generate the actual json
            payload = ollama_utils.generate_config(data)
            response = requests.post(api_url, json=payload)

            if response.status_code != 200:
                if response.status_code == 404: llama_pull()
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
