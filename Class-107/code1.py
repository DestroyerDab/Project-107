import pandas as pd
import csv
import plotly.graph_objects as go

data = pd.read_csv("datasdsfw.csv")

newDataFrame = data.groupby("level")["attempt"].mean()

print(newDataFrame)

figure = go.Figure(go.Bar(x = newDataFrame, y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = "h"))

figure.show()