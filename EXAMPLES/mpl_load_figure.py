import matplotlib.pyplot as plt
import pickle

with open('saved_plot.fig', 'rb') as fig_in:
    saved_fig = pickle.load(fig_in)
    print(dir(saved_fig.gca()))
    saved_fig.show()
