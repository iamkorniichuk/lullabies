def key_value_to_dict(data, key="key", value="value"):
    result = {}
    for obj in data:
        result[obj[key]] = obj[value]
    return result
