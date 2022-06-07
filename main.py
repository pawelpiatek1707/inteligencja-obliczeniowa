from modules.warehouse_generator import generate_warehouse_data
from modules.warehouse_generator import generate_storage_warehouse_data
from modules.json_actions import read_json
from modules.vizualization import display_points_plot
from modules.cars_collection import CarsCollection

warehouse_data: list[dict[str, int]] = generate_warehouse_data()
warehouse_storage_data: list[dict[str, int]] = generate_storage_warehouse_data()
warehouse_all_locations: list[dict[str, int]] = warehouse_storage_data + warehouse_data
company_cars = CarsCollection()
company_cars.place_in_start_warehouses()

print(company_cars)
