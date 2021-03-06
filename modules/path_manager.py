from math import sqrt

from modules.cars_collection import CarsCollection
from modules.car import Car
from modules.vizualization import display_car_path, display_road, display_multiple_roads


class PathManager:
    def __init__(self, warehouse_data: list[dict[str, int]], cars_data: CarsCollection) -> None:
        self._warehouse_data: list[dict[str, int]] = warehouse_data
        self._cars_data: CarsCollection = cars_data

    def calculate_distance(self, point_a: dict[str, int], point_b: dict[str, int]) -> int:
        dist_x: int = abs(point_a["x"] - point_b["x"])
        dist_y: int = abs(point_a["y"] - point_b["y"])
        return int(sqrt(dist_x**2 + dist_y**2))

    def place_cars_in_start_locations(self) -> None:
        for car_id in self._cars_data.cars:
            self._cars_data.cars[car_id].add_path_log(
                self._warehouse_data[self._cars_data.cars[car_id].current_location_id],
                self._cars_data.cars[car_id].max_capacity, 0
            )

    def check_if_all_warehouses_done(self) -> bool:
        for warehouse in self._warehouse_data:
            if warehouse["storage"]:
                continue
            if warehouse["products_to_receive"] > 0:
                return False
            if warehouse["products_to_ship"] > 0:
                return False
        return True

    def decision_making_rules(self, car: Car) -> dict[str, bool]:
        if car.max_capacity - car.load <= 200:
            return {
                "can_deliver": True,
                "can_recharge": False,
                "should_deliver": True,
                "should_recharge": False,
                "should_return": False
            }
        if 200 < car.max_capacity - car.load <= car.max_capacity * 0.5:
            return {
                "can_deliver": True,
                "can_recharge": True,
                "should_deliver": True,
                "should_recharge": False,
                "should_return": False
            }
        if car.max_capacity * 0.5 < car.max_capacity - car.load <= car.max_capacity - 400:
            return {
                "can_deliver": True,
                "can_recharge": True,
                "should_deliver": True,
                "should_recharge": True,
                "should_return": False
            }
        if car.max_capacity - 400 < car.max_capacity - car.load <= car.max_capacity - 200:
            return {
                "can_deliver": True,
                "can_recharge": True,
                "should_deliver": False,
                "should_recharge": True,
                "should_return": False
            }
        if True:
            return {
                "can_deliver": False,
                "can_recharge": True,
                "should_deliver": False,
                "should_recharge": True,
                "should_return": True
            }

    def find_warehouse_with_condition(self, decision: dict[str, bool], position_id: int) -> int:
        contest: list[dict[str, int]] = []
        minimum: int = 1000
        minimum_id: int = 0

        if decision["should_return"]:
            for warehouse in self._warehouse_data:
                if warehouse["storage"]:
                    contest.append({
                        "id": str(warehouse["id"]),
                        "distance": self.calculate_distance(warehouse, self._warehouse_data[position_id])
                    })
        else:
            if decision["can_deliver"]:
                for warehouse in self._warehouse_data:
                    if warehouse["storage"]:
                        continue
                    if warehouse["products_to_receive"] > 0:
                        distance: int = self.calculate_distance(warehouse, self._warehouse_data[position_id])
                        contest.append({
                            "id": str(warehouse["id"]),
                            "distance": distance / 2 if decision["should_deliver"] else distance
                        })

            if decision["can_recharge"]:
                for warehouse in self._warehouse_data:
                    if warehouse["storage"]:
                        continue
                    if warehouse["products_to_ship"] > 0:
                        distance: int = self.calculate_distance(warehouse, self._warehouse_data[position_id])
                        contest.append({
                            "id": str(warehouse["id"]),
                            "distance": distance / 3 if decision["should_recharge"] else distance
                        })

        for item in contest:
            if item["distance"] < minimum:
                minimum = item["distance"]
                minimum_id = item["id"]

        return minimum_id

    def calculate_load_unload(self, point_id: int, car_id: int) -> tuple[int, int]:
        warehouse: dict[str, int] = self._warehouse_data[point_id]
        car: Car = self._cars_data.cars[car_id]

        if warehouse["storage"]:
            return car.max_capacity - car.load, 0

        if warehouse["products_to_receive"] > 0:
            return 0, warehouse["products_to_receive"]

        if warehouse["products_to_ship"] > 0:
            return warehouse["products_to_ship"], 0

        return 0, 0

    def solve_problem(self) -> None:
        self.place_cars_in_start_locations()

        while not self.check_if_all_warehouses_done():
            print('[trasa] istniej?? jeszcze nieobs??u??one magazyny, wyliczam dalej tras?? pojazd??w')

            for car in self._cars_data.cars:
                decision: dict[str, bool] = self.decision_making_rules(self._cars_data.cars[car])
                print(f"[samoch??d-{self._cars_data.cars[car].plates_number}] podejmuje decyzj??: " + str(decision))
                destination_id: int = int(self.find_warehouse_with_condition(decision,
                    self._cars_data.cars[car].current_location_id))
                destination: dict[str, int] = self._warehouse_data[destination_id]
                load, unload = self.calculate_load_unload(destination_id, car)
                if not destination["storage"]:
                    self._warehouse_data[destination_id]["products_to_ship"] -= load
                    self._warehouse_data[destination_id]["products_to_receive"] -= unload
                    destination: dict[str, int] = self._warehouse_data[destination_id]
                if destination_id == 0:
                    self._cars_data.cars[car].add_path_log(destination, 0, self._cars_data.cars[car].load / 2)
                else:
                    self._cars_data.cars[car].add_path_log(destination, load, unload)

        print("[trasa] wszystkie magazyny obs??u??one, pojazdy wracaj?? do magazyn??w")

        for car in self._cars_data.cars:
            if self._cars_data.cars[car].current_location_id != 0:
                self._cars_data.cars[car].add_path_log(self._warehouse_data[0], 0, self._cars_data.cars[car].load)

        print("[trasa] pojazdy zako??czy??y prac?? i wykona??y nast??puj??c?? tras??")

        for car in self._cars_data.cars:
            print(self._cars_data.cars[car].get_path_log())
            display_road(self._cars_data.cars[car].get_path())
        display_multiple_roads(self._cars_data.cars)
