import pandas as pd
import csv
import plotly.express as pe

data = pd.read_csv("datasdsfw.csv")

newDataFrame = data.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

figure = pe.scatter(newDataFrame, x = "student_id", y = "level", size = "attempt", color = "attempt")

figure.show()