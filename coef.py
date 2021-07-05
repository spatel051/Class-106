import numpy as np
import csv
import plotly.express as px

def get_data_source(data_path):
    temperature = []
    ice_cream_sales = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            temperature.append(float(row['Temperature']))
            ice_cream_sales.append(float(row['Ice-cream Sales( â‚¹ )']))
    
    return {"x": temperature, "y": ice_cream_sales}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between temperature and ice cream sales is " + str(correlation[0, 1]))

def set_up():
    data_path = 'data1.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)

set_up()