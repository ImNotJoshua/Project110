import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv  
df = pd.read_csv("medium_data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("population mean", population_mean)
print("standard deviation", std_deviation)
def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean],y=[0,1],mode="lines", name="MEAN"))
    fig.show()
dataset=[]
for i in range(0, counter):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
mean=statistics.mean(dataset)
std_deviation=statistics.stdev(dataset)
print("mean of a sample",mean)
print("standard deviation of a sample", std_deviation)
def setup():
    mean_list=[]
    for i in range(0,100):
        set_off_mean=random_set_off_mean(30)
        mean_list.append(set_off_mean)
        show_fig(mean_list)