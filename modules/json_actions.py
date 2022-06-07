import json
from modules.warehouse_generator import generate_warehouse_data


def generate_json():

    warehouse = generate_warehouse_data()

    with open('data/data.json', 'w') as f:
        json.dump(warehouse, f)
        f.close()


def read_json():
    f = open('data/data.json')

    data = json.load(f)
    f.close()
    return data
