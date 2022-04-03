import random
import json

points_arr = []
for id in range(100):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    is_reciver = random.randint(0,1)
    if is_reciver == 0:
        products_to_receive = 0
        products_to_ship = random.randint(100, 200)
    else:
        products_to_receive = random.randint(100, 200)
        products_to_ship = 0
    point = {
        "id": id,
        "x": x,
        "y": y,
        "products_to_receive": products_to_receive,
        "products_to_ship": products_to_ship
    }
    points_arr.append(point)

with open('data/data.json', 'w') as f:
    json.dump(points_arr, f)

