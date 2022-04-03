import random


def check_if_unique_warehouse(warehouse_item: dict[str, int], warehouse_list: list[dict[str, int]]) -> bool:
    for warehouse in warehouse_list:
        if warehouse['x'] == warehouse_item['y'] and warehouse['y'] == warehouse_item['y']:
            return False
    return True


def search_duplicates_and_regenerate(verify_list: list[dict[str, int]]) -> list[dict[str, int]]:
    for key, warehouse in enumerate(verify_list):
        if not check_if_unique_warehouse(warehouse, verify_list):
            while not check_if_unique_warehouse(warehouse, verify_list):
                warehouse['x'] = random.randint(0, 100)
                warehouse['y'] = random.randint(0, 100)
            verify_list[key] = warehouse
    return verify_list


def generate_warehouse_data() -> list[dict[str, int]]:
    warehouse: list[dict[str, int]] = []

    for i in range(100):
        if random.randint(0, 1) == 1:
            is_delivery: bool = True
        else:
            is_delivery: bool = False

        if is_delivery:
            receive: int = 0
            ship: int = random.randint(100, 200)
        else:
            receive: int = random.randint(100, 200)
            ship: int = 0

        warehouse.append({
            "id": i,
            "x": random.randint(0, 100),
            "y": random.randint(0, 100),
            "products_to_receive": receive,
            "products_to_ship": ship
        })

    return search_duplicates_and_regenerate(warehouse)
