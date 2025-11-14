import pandas as pd
import numpy as np
# Read and store the csv
data_frame = pd.read_csv("./Pandas Hackathon Files/HackathonDataset.csv")
# Convert each entry into a float without "$"
data_frame = (data_frame['order_amt'].str[1:]).astype(float)
# Sum the values
total_sales = data_frame.sum()

