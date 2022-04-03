import json
from modules.warehouse_generator import generate_warehouse_data

def generate_json():

    warehouse = generate_warehouse_data()

    with open('data/data.json', 'w') as f:
        json.dump(warehouse, f)