import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def display_points_plot(data):
    df = pd.DataFrame(data)
    x, y = df['x'], df['y']
    plt.plot(x,y, 'bo')
    plt.show()



def display_road(data):
    df = pd.DataFrame(data)
    x, y = df['x'], df['y']
    fig, ax = plt.subplots()
    line, = ax.plot(data[0]['x'], data[0]['y'])

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

