from modules.warehouse_generator import generate_warehouse_data
from modules.warehouse_generator import generate_storage_warehouse_data
from modules.vizualization import display_points_plot, display_road, display_multiple_roads
from modules.cars_collection import CarsCollection
from modules.path_manager import PathManager

warehouse_data: list[dict[str, int]] = generate_warehouse_data()
warehouse_storage_data: list[dict[str, int]] = generate_storage_warehouse_data()
warehouse_all_locations: list[dict[str, int]] = warehouse_storage_data + warehouse_data

display_points_plot(warehouse_data, warehouse_storage_data)

company_cars: CarsCollection = CarsCollection()
company_cars.place_in_start_warehouses()
path_manager: PathManager = PathManager(warehouse_all_locations, company_cars)
path_manager.solve_problem()
