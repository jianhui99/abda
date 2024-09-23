import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'funds.json')

def read_data():
    """
    Read data from the funds.json file.
    """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def write_data(data):
    """
    Write data to the funds.json file.
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)