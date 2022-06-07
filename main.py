from modules.warehouse_generator import generate_warehouse_data
from modules.json_actions import read_json
from modules.vizualization import display_points_plot

warehouse_data: list[dict[str, int]] = generate_warehouse_data()

json_array = read_json()
display_points_plot(json_array)
