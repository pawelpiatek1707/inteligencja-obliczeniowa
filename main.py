from modules.warehouse_generator import generate_warehouse_data
from modules.json_actions import read_json
from modules.vizualization import display_points_plot, display_road

# print(generate_warehouse_data())

json_array = read_json()
# display_points_plot(json_array)
test_list = json_array[0:10]
test_list.append(test_list[0])
display_road(test_list)
