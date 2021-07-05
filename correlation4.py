import csv
import plotly.express as px

with open('data4.csv') as f:
    df = csv.DictReader(f)

    fig = px.scatter(df, x = 'Days Present', y = "Marks In Percentage")
    fig.show()