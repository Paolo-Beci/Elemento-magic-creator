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
def llama_pull(version="13b"):
    api_url = "http://ollama:11434/api/pull"
    if request.args.get("version") is not None:
        version = request.args.get("version")

    name = {
        "name": f"llama2:{version}",
        "stream": False,
    }

    try:
        response = requests.post(api_url, json=name)
        if response.status_code != 200:
            app.logger.info(
                f"Failed to pull the model, status code: {response.status_code} \n error: {response.json()}"
            )
            return (
                jsonify({"error": "Failed to pull Llama2"}),
                response.status_code,
            )
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        app.logger.info(f"Failed to pull the model, status code: 500 \n error: {e}")
        return jsonify({"error": f"Request to Llama2 API failed: {e}"}), 500


@app.route("/api/v1/generate", methods=["GET"])
def ollama_request():
    api_url = "http://ollama:11434/api/generate"

    try:
        data = request.json
        if data is None:
            app.logger.info("error: No data provided in body request")
            return jsonify({"error": "No data provided in body request"}), 404

        direct = request.args.get("direct")
        if direct is None or direct == "false":
            # * First step: refinement of the body
            filtered_text = utils.get_core_info(data)
            payload = ollama_utils.extract_requirements(filtered_text)
            response = requests.post(api_url, json=payload)

            check_ollama_response(response)

            data = response.json()["response"]

        # * Second step: generate the actual json
        payload = ollama_utils.generate_config(data)
        response = requests.post(api_url, json=payload)

        check_ollama_response(response)

        # * Third step: refinement of the json
        result = response.json()
        result = utils.refinement(json.loads(result["response"]))
        return jsonify(result)

    except requests.exceptions.RequestException as e:
        app.logger.info(f"Failed to pull the model, status code: 500 \n error: {e}")
        return jsonify({"error": f"Request to Ollama API failed: {e}"}), 500


##* UTILS (local) *##
def check_ollama_response(response):
    if response.status_code != 200:
        app.logger.info(
            f"Failed to reach Ollama, status code: {response.status_code} \n error: {response.json()}"
        )
        if response.status_code == 404:
            app.logger.info(f"Trying to pull the model...")
            llama_pull("13b")
        return (
            jsonify({"error": "Failed to fetch data from Ollama API"}),
            response.status_code,
        )


##* APP (just for testing purpose - use flask run instead) *##
if __name__ == "__main__":
    app.run(port=5001, debug=True)
