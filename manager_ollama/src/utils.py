target_words = [
    "gpu",
    "cpu",
    "system",
    "requirement",
    "requirements",
    "os",
    "frequency",
    "version",
    "minimum",
    "recommended",
    "memory",
    "ram",
    "disk",
    "GB",
    "GHz",
    "settings"
]


def get_core_info(data):
    # Remove duplicates
    unique_text = list(set(data))
    # Filter paragraphs that do not contain target words
    filtered_text = [
        text
        for text in unique_text
        if any(word in text.lower() for word in target_words)
    ]
    filtered_text = ". ".join(filtered_text)

    return filtered_text
