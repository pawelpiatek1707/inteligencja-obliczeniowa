import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

warehouse_data = None
storage_data = None


def display_points_plot(data, data_2):
    global warehouse_data
    global storage_data
    df = pd.DataFrame(data)
    df2 = pd.DataFrame(data_2)
    warehouse_data = df
    storage_data = df2
    x, y = df['x'], df['y']
    x2, y2 = df2['x'], df2['y']
    plt.plot(x, y, 'bo')
    plt.plot(x2, y2, 'ro')
    plt.show()


def display_car_path(data):
    global warehouse_data
    global storage_data
    df = warehouse_data
    df2 = storage_data
    df3 = pd.DataFrame(data)
    x, y = df['x'], df['y']
    x2, y2 = df2['x'], df2['y']
    plt.plot(x, y, 'bo')
    plt.plot(x2, y2, 'ro')
    x3, y3 = df3['x'], df3['y']
    plt.plot(x3, y3, '-k')
    plt.show()


def display_road(data):
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()

    x_data = []
    y_data = []

    x_data.append(data[0]['x'])
    y_data.append(data[0]['y'])


    def animation_frame(i):
        if i < len(data):
            x_data.append(data[i]['x'])
            y_data.append(data[i]['y'])
            plt.plot(x_data,y_data, color="blue")


    ani = FuncAnimation(fig, animation_frame, frames=len(data), interval=100, repeat=False)
    plt.show()


def return_random_color():
    return "%06x" % random.randint(0, 0xFFFFFF)



def display_multiple_roads(data):

    colors_list = ['FE0002', 'F9941E', 'FFFF01', '00FF03', '000000', '642D92']

    plt.figure(figsize=(20, 15))
    plt.title("Wizualizacja trasy przejazdu")
    full_list = sum(data, [])
    full_list_df = pd.DataFrame(full_list)
    x, y = full_list_df['x'], full_list_df['y']
    plt.plot(x,y, 'bo')

    for index, row in enumerate(data):
        df = pd.DataFrame(row)
        x_array = df['x']
        y_array = df['y']

        random_color = None
        if index > len(colors_list) - 1:
            random_color = return_random_color()
        else:
            random_color = colors_list[index]

        plt.plot(x_array,y_array, color=f"#{random_color}")


    plt.show()


