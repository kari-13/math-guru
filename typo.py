from rapidfuzz import process

def flatten_json(data, current_path=None, result=None):
    """
    Flatten a nested JSON (dicts and lists) into a single-level dictionary.
    Keys represent the full path separated by spaces.
    """
    if result is None:
        result = {}
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{current_path} {key}" if current_path else key
            flatten_json(value, new_path, result)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{current_path} {index}" if current_path else str(index)
            flatten_json(item, new_path, result)
    else:
        result[current_path] = data
    return result


def match_full(user_input, flat_data, threshold=60):
    """
    Fuzzy match the entire user input against flattened keys.
    Returns matched_key, value, and score if matched; otherwise None, None, None.
    """
    keys = list(flat_data.keys())
    match = process.extractOne(user_input, keys)
    if match and match[1] >= threshold:
        return match[0], flat_data[match[0]], match[1]
    return None, None, None


def match_level_by_level(user_keys, data, threshold=60):
    """
    Fuzzy match user keys one by one on nested dict levels.
    Returns matched value or None if any key doesn't match well enough.
    """
    current = data
    for key in user_keys:
        if not isinstance(current, dict):
            # Can't go deeper if current level is not dict
            return None
        possible_keys = current.keys()
        match = process.extractOne(key, possible_keys)
        if match and match[1] >= threshold:
            current = current[match[0]]
        else:
            return None
    return current
