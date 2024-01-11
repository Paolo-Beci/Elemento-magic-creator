def get_generic_rules():
    with open("templates/generic_rules.txt", "r") as f:
        rules = f.read()
        return rules


def get_structure():
    with open("templates/structure.txt", "r") as f:
        structure = f.read()
        return structure


def get_rules():
    with open("templates/rules.md", "r") as f:
        template = f.read()
        return template


def get_gpu_vendors():
    with open("templates/gpu_vendors.txt", "r") as f:
        gpu_vendors = f.read()
        return gpu_vendors

def get_gpu_vendors_extended():
    with open("templates/gpu_vendors_extended.txt", "r") as f:
        gpu_vendors = f.read()
        return gpu_vendors

def get_gpu_vendors_json():
    with open("templates/gpu_vendors.json", "r") as f:
        gpu_vendors = f.read()
        return gpu_vendors