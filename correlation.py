import csv
import plotly.express as px

with open('data1.csv') as f:
    df = csv.DictReader(f)

    fig = px.scatter(df, x = 'Temperature', y = 'Ice-cream Sales( â‚¹ )')
    fig.show()