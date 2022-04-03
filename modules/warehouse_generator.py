import random


def generate_warehouse_data():
    warehouse: list[dict[str, int]] = []

    for i in range(100):
        if random.randint(0, 1) == 1:
            is_delivery: bool = True
        else:
            is_delivery: bool = False

        if is_delivery:
            receive: int = 0
            ship: int = random.randint(0, 200)
        else:
            receive: int = random.randint(0, 200)
            ship: int = 0

        warehouse.append({
            "id": i,
            "x": random.randint(0, 100),
            "y": random.randint(0, 100),
            "products_to_receive": receive,
            "products_to_ship": ship
        })

    return warehouse
