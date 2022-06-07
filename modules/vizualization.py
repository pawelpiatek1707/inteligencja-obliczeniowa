import pandas as pd
import matplotlib.pyplot as plt


def display_points_plot(data):
    df = pd.DataFrame(data)
    x, y = df['x'], df['y']
    plt.plot(x,y, 'bo')
    plt.show()