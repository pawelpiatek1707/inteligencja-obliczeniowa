from modules.warehouse_generator import generate_warehouse_data
from modules.json_actions import read_json
from modules.vizualization import display_points_plot, display_road, display_multiple_roads
# print(generate_warehouse_data())

json_array = read_json()

n = 20

# using list comprehension
splited_list = [json_array[i * n:(i + 1) * n] for i in range((len(json_array) + n - 1) // n )]

# display_points_plot(json_array)
# test_list = json_array[0:9]
# test_list.append(test_list[0])

# test_list2 = json_array[10:20]
# test_list2.append(test_list2[0])
# display_road(test_list)
# display_road(test_list2)

display_multiple_roads(splited_list)
