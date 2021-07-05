import numpy as np
import csv
import plotly.express as px

def get_data_source(data_path):
    days_present = []
    percentage = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            days_present.append(float(row['Days Present']))
            percentage.append(float(row['Marks In Percentage']))
    
    return {"x": days_present, "y": percentage}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between days present and marks " + str(correlation[0, 1]))

def set_up():
    data_path = 'data4.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)

set_up()