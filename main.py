import pandas as pd
import plotly.express as px
import csv

with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]