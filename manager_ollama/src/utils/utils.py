import math, json
from difflib import SequenceMatcher
from templates import templates

target_words = [
    # GENERAL
    "gpu",
    "cpu",
    "os",
    "system",
    "requirement",
    "requirements",
    "version",
    "minimum",
    "recommended",
    "memory",
    "ram",
    "GB",
    "GHz",
    "settings",
    "frequency",
    "instruction",
    "set",
    # OS
    "Windows",
    "linux",
    "mac",
    # CPU
    "intel",
    "amd",
    # GPU
    "nvidia",
    "geforce",
    "rtx",
    "gtx",
    "amd",
    "radeon",
]


def get_core_info(data):
    filtered_text = [
        text for text in data if any(word in text.lower() for word in target_words)
    ]
    filtered_text = ". ".join(filtered_text)

    return filtered_text


def similar(a, b):
    return SequenceMatcher(
        None, a, b
    ).ratio()  # returns a float between 0 and 1 that indicates the similarity


def get_gpu_info(pci):
    gpu_list = templates.get_gpu_vendors_json()
    gpu_list = json.loads(gpu_list)
    score_per_gpu = []
    for item in pci:
        for gpu in gpu_list:
            score = similar(item["model"], gpu["name"])
            if score > 0.8:
                score_per_gpu.append(
                    {
                        "score": score,
                        "model": gpu["model"],
                        "vendor": gpu["vendor"],
                    }
                )

    if len(score_per_gpu) == 0:
        return "25C9", "10DE"  # Default value: "NVIDIA GeForce RTX 3050 Ti"

    sorted_score_per_gpu = sorted(score_per_gpu, key=lambda k: k["score"], reverse=True)
    return sorted_score_per_gpu[0]["model"], sorted_score_per_gpu[0]["vendor"]


def refinement(data):
    # * Refinement of the json (change keys in order to be consistent with the reference json)
    data["slots"] = data.pop("processor_cores")
    data["flags"] = data.pop("instruction_sets")
    data["min_frequency"] = data.pop("min_cpu_frequency")
    data["ramsize"] = data.pop("ram_size")

    # * Refinement of the values
    data["ramsize"] = (
        data["ramsize"][0] if isinstance(data["ramsize"], list) else data["ramsize"]
    ) * math.pow(1024, 3)
    data["pci"][0]["model"], data["pci"][0]["vendor"] = get_gpu_info(data["pci"])
    del data["pci"][1:]  # ToDo: consider the case of Audio cards

    return data
