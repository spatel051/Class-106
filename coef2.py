import numpy as np
import csv
import plotly.express as px

def get_data_source(data_path):
    size_tv = []
    time_watching = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            size_tv.append(float(row['Size of TV']))
            time_watching.append(float(row['Average time spent watching TV in a week (hours)']))
    
    return {"x": size_tv, "y": time_watching}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between tv size and average time spent watching tv " + str(correlation[0, 1]))

def set_up():
    data_path = 'data3.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)

set_up()