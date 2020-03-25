import json

def from_json(value):
    try:
        return json.loads(value)
    except Exception as e:
        return value

def to_json(value):
    try:
        return json.dumps(value)
    except Exception as e:
        return value
