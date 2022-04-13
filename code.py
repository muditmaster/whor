from cv2 import mean
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv('newdata.csv')
data = df["temp"].tolist()



def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    sample_mean = statistics.mean(dataset)
    return sample_mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"],show_hist = False)
    fig.show()


def setup():
    mean_list = []
    for i in range(100):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()

population_mean = statistics.mean(data)
print("population mean:- ", population_mean)
