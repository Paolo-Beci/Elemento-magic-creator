from templates import templates


def extract_requirements(filtered_text):
    prompt = (
        "Get all core information about techinical System Requirements from this text:"
        + filtered_text
    )

    payload = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False,
    }

    return payload


def generate_config(data):
    prompt = (
        "Considering the requirements:"
        + data
        + "Create a JSON following rules:"
        + templates.get_rules()
        + "Return only the json with this structure:"
        + templates.get_structure()
    )

    payload = {
        "model": "llama2",
        "prompt": prompt,
        "format": "json",
        "stream": False,
    }

    return payload
