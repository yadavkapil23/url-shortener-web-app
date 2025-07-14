import json
from pathlib import Path

DATA_PATH = Path("data/urls.json")

def load_data():
    if not DATA_PATH.exists() or DATA_PATH.stat().st_size == 0:
        return {}
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

def increment_click(code: str):
    data = load_data()
    if code in data:
        data[code]['clicks'] += 1
        save_data(data)
        return data[code]['original_url']
    return None
