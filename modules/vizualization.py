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
    global warehouse_data
    global storage_data
    df = warehouse_data
    df2 = storage_data
    x, y = df['x'], df['y']
    x2, y2 = df2['x'], df2['y']

    fig, ax = plt.subplots()

    x_data = []
    y_data = []

    x_data.append(data[0]['x'])
    y_data.append(data[0]['y'])


    def animation_frame(i):
        if i < len(data):
            x_data.append(data[i]['x'])
            y_data.append(data[i]['y'])
            plt.plot(x_data,y_data, color="black")


    ani = FuncAnimation(fig, animation_frame, frames=len(data), interval=100, repeat=False)
    plt.plot(x, y, 'bo')
    plt.plot(x2, y2, 'ro')
    plt.show()


def return_random_color():
    return "%06x" % random.randint(0, 0xFFFFFF)



def display_multiple_roads(data):

    global warehouse_data
    global storage_data
    df = warehouse_data
    df2 = storage_data
    x, y = df['x'], df['y']
    x2, y2 = df2['x'], df2['y']

    colors_list = ['FE0002', 'F9941E', 'FFFF01', '00FF03', '000000', '642D92']

    plt.figure(figsize=(15, 10))
    plt.title("Wizualizacja tras przejazdów")
    for index, row in enumerate(data):
        df = pd.DataFrame(data[row].get_path())
        x_array = df['x']
        y_array = df['y']

        random_color = None
        if index > len(colors_list) - 1:
            random_color = return_random_color()
        else:
            random_color = colors_list[index]

        plt.plot(x_array,y_array, color=f"#{random_color}")

    plt.plot(x, y, 'bo')
    plt.plot(x2, y2, 'ro')
    plt.show()


