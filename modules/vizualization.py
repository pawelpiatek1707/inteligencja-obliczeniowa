import pandas as pd
import matplotlib.pyplot as plt


def display_points_plot(data, data_2):
    df = pd.DataFrame(data)
    df2 = pd.DataFrame(data_2)
    x, y = df['x'], df['y']
    x2, y2 = df2['x'], df2['y']
    plt.plot(x, y, 'bo')
    plt.plot(x2, y2, 'ro')
    plt.show()
