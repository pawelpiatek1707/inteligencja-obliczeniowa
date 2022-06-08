import pandas as pd
import matplotlib.pyplot as plt

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
